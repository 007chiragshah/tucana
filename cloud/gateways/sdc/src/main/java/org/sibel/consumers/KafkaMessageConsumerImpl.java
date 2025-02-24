package org.sibel.consumers;

import com.google.inject.Inject;
import java.time.Duration;
import java.util.*;
import org.apache.kafka.clients.CommonClientConfigs;
import org.apache.kafka.clients.admin.KafkaAdminClient;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.KafkaException;
import org.apache.kafka.common.config.SslConfigs;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.sibel.config.Settings;
import org.sibel.exceptions.KafkaUnavailable;

public class KafkaMessageConsumerImpl implements KafkaMessageConsumer {
    private static final Logger LOG = LogManager.getLogger();

    private KafkaConsumer<String, String> kafkaConsumer = null;

    private final Settings settings;

    @Inject
    public KafkaMessageConsumerImpl(Settings settings) {
        this.settings = settings;
    }

    private KafkaConsumer<String, String> createConsumer() throws KafkaUnavailable {
        try {
            var properties = getKakfaProperties();
            return new KafkaConsumer<>(properties);
        } catch (KafkaException e) {
            throw new KafkaUnavailable("Failed to create Kafka consumer", e);
        }
    }

    private Properties getKakfaProperties() {
        var properties = new Properties();
        var bootstrapServers = String.format("%s:%s,", settings.KAFKA_HOST(), settings.KAFKA_PORT());
        properties.setProperty(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        properties.setProperty(ConsumerConfig.GROUP_ID_CONFIG, UUID.randomUUID().toString());
        properties.setProperty(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        properties.setProperty(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        if (!Objects.equals(settings.ENVIRONMENT(), "local")) {
            properties.setProperty(CommonClientConfigs.SECURITY_PROTOCOL_CONFIG, "SSL");
            properties.put(SslConfigs.SSL_KEYSTORE_TYPE_CONFIG, "PKCS12");
            properties.put(SslConfigs.SSL_KEYSTORE_LOCATION_CONFIG, settings.KAFKA_KEY_FILE_PATH());
            properties.put(SslConfigs.SSL_KEYSTORE_PASSWORD_CONFIG, settings.KAFKA_PASSWORD());
            properties.put(SslConfigs.SSL_TRUSTSTORE_TYPE_CONFIG, "PEM");
            properties.put(SslConfigs.SSL_TRUSTSTORE_CERTIFICATES_CONFIG, settings.KAFKA_CA_FILE());
        }
        return properties;
    }

    private KafkaConsumer<String, String> getConsumer() throws KafkaUnavailable {
        if (kafkaConsumer == null) {
            kafkaConsumer = createConsumer();
        }
        return kafkaConsumer;
    }

    @Override
    public boolean isHealthy() {
        var healthy = false;
        try (var kafkaAdmin = KafkaAdminClient.create(getKakfaProperties())) {
            var topics = kafkaAdmin.listTopics().names().get();
            if (topics.isEmpty()) {
                LOG.error("Topic list is empty");
            } else {
                healthy = true;
            }
        } catch (Exception e) {
            LOG.error("Error connecting to kafka consumer", e);
        }
        return healthy;
    }

    @Override
    public void subscribeToTopic(String topic) throws KafkaUnavailable {
        try {
            getConsumer().subscribe(Collections.singletonList(topic));
        } catch (KafkaUnavailable e) {
            throw e;
        } catch (Exception e) {
            throw new KafkaUnavailable("Failed to subscribe to topic", e);
        }
    }

    @Override
    public ConsumerRecords<String, String> poll(Duration duration) throws KafkaUnavailable {
        try {
            return getConsumer().poll(duration);
        } catch (KafkaUnavailable e) {
            throw e;
        } catch (Exception e) {
            throw new KafkaUnavailable("Failed poll messages", e);
        }
    }
}
