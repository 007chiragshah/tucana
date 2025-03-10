#!/usr/bin/env bash

# Get the app path
env_path=$(dirname $(dirname "$0"))/.env

# create .env file
{
  # app config
  echo "DEBUG=False"
  echo "LOGURU_LEVEL=DEBUG"
  echo "GUNICORN_WORKERS=1"
  echo "ENVIRONMENT=local"
  echo "APPLICATION_PORT=8007"
  echo "BASE_PATH=/patient"
  echo "PUBLISHER_BACKEND=app.common.event_sourcing.publisher.KafkaPublisher"
  echo "PATIENT_PUBLISHER_AUDIT_TRAIL_STREAM_NAME=events-patient"
  echo "DEVICE_PUBLISHER_AUDIT_TRAIL_STREAM_NAME=events-patient"
  echo "SIBEL_VERSION=0.1.0"
  echo "DEVICE_APIS_ENABLED=true"

  # Sentry config
  echo "SENTRY_DSN="
  echo "SENTRY_TRACE_SAMPLE_RATE=1.0"
  echo "SENTRY_PROFILES_SAMPLE_RATE=1.0"

  # Database config
  echo "DB_HOST=localhost"
  echo "DB_PORT=5432"
  echo "DB_NAME=test_patient"
  echo "DB_USERNAME=postgres"
  echo "DB_PASSWORD=cantguessthis"
  echo "DB_ENCRYPTION_KEY=hola123"

  # Kafka config
  echo "KAFKA_HOST=localhost"
  echo "KAFKA_PORT=9092"
  echo "KAFKA_PASSWORD=cantguessthis"
  echo "KAFKA_CA_FILE_PATH=''"
  echo "KAFKA_CERT_FILE_PATH=''"
  echo "KAFKA_KEY_FILE_PATH=''"

  # Kafka topics
  echo "EVENTS_ALERT_TOPIC=alerts"
  echo "EVENTS_SDC_TOPIC=events-sdc"
  echo "EVENTS_DEVICE_TOPIC=events-device"
  echo "KAFKA_HEALTHCHECK_TOPIC='healthcheck'"

  # Auth verification
  echo "JWT_VERIFYING_KEY=LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQ0lqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FnOEFNSUlDQ2dLQ0FnRUFweURoL0FKWUV1cW4yVEZVeGprNwo5eno2V1VGcmJ3Rk5DaFdyWWUvY3ROK3ZpdnJVdU9qS3phcUdndXBPS0pyVmVITzAxMmQzVmtEajMzWnVDNE53CmxxZjYvOUY4QnFCd3BoWHVsNkhOelB6YmdBL29tR0E3UjhpdmlnaXdULytjaWx4QnhXTThYV0VGZk1OZ0J0aFUKbGtDeFB5MnRkRjNJNTdTbVBtUzdhNjNsZ3RWTnFJdm8xV1VWUjN5Wk96UDg4ZTVjQWxNdlhoaS9OYytkWVNyRgpZdVpON1FwbTJCMmVIQzVmQlI4TXFRQ0lWL2JvN2hWbHd3ZHp2WXlaR2Q3enh3M3BUREZheWJKNzFWaHY2TmhWCmpYdkIrckVDTW9KMWFxRExjdkFwcE1yT29wUkNGNnFHSlRkNGhtaGVQQ1BzeS9vdXROcWE5U0crdXFKVUVHb20KSjNyaGJadzdJdlo3T0VSQXN2eE9rbCs4MVNjcTd6UitvSkQ3RHNMVy84UG9FeWwydzhvV3JaQ1ZlNGM0U1QvZwpKOGxlVDlBbkNBcnN1QVpDR2JJZ3B2MnRDKzVycDBlNGRHckZ2VGg1WlpWbHpvam85bUl2Y1NkeVlEYWJjR0xlCjEzNmgwU1VjNDNYbDJrTXlaRDUrN2ZoelNMMkNWOFAzbzZ4TStvVzU2UndCMTlLUE9xVndSK3R5UFNUTUwxeloKTGw5bmkvbW1ndk1uTTQrTlpkMFliaXZ3Zy9GaHpGRGtPZ3BUS2Y1Y29TZnVJSk9ia2J5M01nYzMzc1ZCbUlnZwpXNnFjR2tzNFlEVC9SSEY1ZUZFNm52YVZTMy9pek5OZjR4VC9lNDl0dHB4b0xJNk1zQW5vZmlDRjBLR3hvUWI1CkU0YnlndXRieS94NUh3NmJNNm9PeDZzQ0F3RUFBUT09Ci0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQo="

  # Redis config
  echo "REDIS_HOST=localhost"
  echo "REDIS_PORT=6379"
  echo "REDIS_USERNAME=user"
  echo "REDIS_PASSWORD=pass"
  echo "REDIS_CACHE_TTL=86400"
  echo "CACHE_ENABLED=False"
  echo "PROJECT_NAME=patient"
} > $env_path

echo "Local $env_path file created."
