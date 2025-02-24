import BloodPressure from '@/app/(authenticated)/home/details/Metrics/BloodPressure';
import BodyPosition from '@/app/(authenticated)/home/details/Metrics/BodyPosition';
import BodyTemperature from '@/app/(authenticated)/home/details/Metrics/BodyTemperature';
import ChestTemperature from '@/app/(authenticated)/home/details/Metrics/ChestTemperature';
import FallDetector from '@/app/(authenticated)/home/details/Metrics/FallDetector';
import LimbTemperature from '@/app/(authenticated)/home/details/Metrics/LimbTemperature';
import PulseRate from '@/app/(authenticated)/home/details/Metrics/PulseRate';
import useMetrics from '@/hooks/useMetricsData';
import useSensorsConnected from '@/hooks/useSensorsConnected';
import {
  BloodPressureUnit,
  FallState,
  Metrics,
  PulseRateUnit,
  TemperatureUnit,
} from '@/types/metrics';
import { DisplayVitalsRange } from '@/types/patientMonitor';
import { Sensor } from '@/types/sensor';
import { TECHNICAL_ALERT_TYPE } from '@/utils/alertUtils';
import {
  ALERT_PRIORITY,
  METRIC_INTERNAL_CODES,
  POSITION_TYPES,
  RANGES_CODES,
  VitalMetricInternalCodes,
} from '@/utils/metricCodes';
import { SafeParser } from '@/utils/safeParser';
import { checkMetricSensorCharging } from '@/utils/sensorUtils';
import Grid from '@mui/material/Grid';
import moment from 'moment';
import { useEffect, useMemo, useState } from 'react';
import { ERROR_VALUE } from '@/constants';

type VitalMetricsPanelProps = {
  hasActivePatientSession?: boolean;
  metrics?: Metrics;
  alertThresholds?: Record<string, DisplayVitalsRange>;
  vitalsAlertSeverities: Record<VitalMetricInternalCodes, ALERT_PRIORITY | undefined>;
  technicalAlerts: Record<TECHNICAL_ALERT_TYPE, boolean>;
  isLoading: boolean;
  activeSensors: Sensor[];
};

function getLimitThresholds(
  allAlertThreshold: DisplayVitalsRange | undefined,
  highAlertThreshold: DisplayVitalsRange | undefined,
  lowAlertThreshold: DisplayVitalsRange | undefined
) {
  const upperLimit =
    highAlertThreshold &&
    highAlertThreshold.upperLimit != ERROR_VALUE &&
    highAlertThreshold.lowerLimit != ERROR_VALUE
      ? (highAlertThreshold.alertConditionEnabled &&
          SafeParser.toFixed(highAlertThreshold.upperLimit, 1)) ||
        undefined
      : (allAlertThreshold?.alertConditionEnabled &&
          SafeParser.toFixed(allAlertThreshold?.upperLimit, 1)) ||
        undefined;
  const lowerLimit =
    lowAlertThreshold &&
    lowAlertThreshold.upperLimit != ERROR_VALUE &&
    lowAlertThreshold.lowerLimit != ERROR_VALUE
      ? (lowAlertThreshold.alertConditionEnabled &&
          SafeParser.toFixed(lowAlertThreshold.lowerLimit, 1)) ||
        undefined
      : (allAlertThreshold?.alertConditionEnabled &&
          SafeParser.toFixed(allAlertThreshold?.lowerLimit, 1)) ||
        undefined;
  return { upperLimit, lowerLimit };
}

const VitalMetricsPanel = ({
  hasActivePatientSession = true,
  metrics = {},
  alertThresholds = {},
  vitalsAlertSeverities,
  technicalAlerts,
  isLoading,
  activeSensors,
}: VitalMetricsPanelProps) => {
  const { sensorMetrics } = useMetrics();

  const [hoursInCurrentPosition, setHoursInCurrentPosition] = useState<string>(
    moment.utc(0).format('HH')
  );
  const [minutesInCurrentPosition, setMinutesInCurrentPosition] = useState<string>(
    moment.utc(0).format('mm')
  );

  const sensorsConnected = useSensorsConnected(activeSensors, hasActivePatientSession);

  useEffect(() => {
    // Updates the time for the position duration when a new duration value is received
    const positionDuration = parseInt(
      metrics[METRIC_INTERNAL_CODES.POSITION_DURATION]?.value as string
    );
    if (positionDuration) {
      if (positionDuration >= 100 * 60) {
        // We cap the shown time to 100 hours
        setHoursInCurrentPosition('99');
        setMinutesInCurrentPosition('59');
      } else {
        setHoursInCurrentPosition(
          Math.floor(positionDuration / 60).toLocaleString('en-US', { minimumIntegerDigits: 2 })
        );
        setMinutesInCurrentPosition(
          Math.floor(positionDuration % 60).toLocaleString('en-US', { minimumIntegerDigits: 2 })
        );
      }
    } else {
      setHoursInCurrentPosition('00');
      setMinutesInCurrentPosition('00');
    }
  }, [metrics[METRIC_INTERNAL_CODES.POSITION_DURATION]?.value]);

  const fallState = useMemo((): FallState | null => {
    if (!hasActivePatientSession || technicalAlerts.FALLS) {
      return FallState.UNKNOWN;
    }
    if (!sensorsConnected[METRIC_INTERNAL_CODES.FALLS] && !isLoading) {
      return null;
    }
    if (metrics[METRIC_INTERNAL_CODES.FALLS]?.value === 0) {
      return FallState.NOT_DETECTED;
    }
    if (!metrics[METRIC_INTERNAL_CODES.FALLS]?.value) {
      return FallState.UNKNOWN;
    }
    if ((metrics[METRIC_INTERNAL_CODES.FALLS]?.value as number) > 0) {
      return FallState.DETECTED;
    }
    return FallState.UNKNOWN;
  }, [hasActivePatientSession, technicalAlerts, sensorsConnected, metrics, isLoading]);

  const { upperLimit: bodyTempUpperLimit, lowerLimit: bodyTempLowerLimit } = getLimitThresholds(
    alertThresholds[RANGES_CODES.TEMPERATURE_BODY],
    alertThresholds[RANGES_CODES.TEMPERATURE_BODY_HIGH],
    alertThresholds[RANGES_CODES.TEMPERATURE_BODY_LOW]
  );
  const { upperLimit: skinTempUpperLimit, lowerLimit: skinTempLowerLimit } = getLimitThresholds(
    alertThresholds[RANGES_CODES.TEMPERATURE_SKIN],
    alertThresholds[RANGES_CODES.TEMPERATURE_SKIN_HIGH],
    alertThresholds[RANGES_CODES.TEMPERATURE_SKIN_LOW]
  );
  const { upperLimit: diaUpperLimit, lowerLimit: diaLowerLimit } = getLimitThresholds(
    alertThresholds[RANGES_CODES.DIA],
    alertThresholds[RANGES_CODES.DIA_HIGH],
    alertThresholds[RANGES_CODES.DIA_LOW]
  );
  const { upperLimit: sysUpperLimit, lowerLimit: sysLowerLimit } = getLimitThresholds(
    alertThresholds[RANGES_CODES.SYS],
    alertThresholds[RANGES_CODES.SYS_HIGH],
    alertThresholds[RANGES_CODES.SYS_LOW]
  );

  return (
    <Grid display='flex' flexDirection='row'>
      <Grid display='flex' flex={4.75} flexDirection='row' mr={10} gap={10}>
        <PulseRate
          isConnected={sensorsConnected[METRIC_INTERNAL_CODES.PULSE]}
          isLoading={isLoading}
          timestamp={metrics[METRIC_INTERNAL_CODES.PULSE]?.timestamp}
          unit={metrics[METRIC_INTERNAL_CODES.PULSE]?.unit as PulseRateUnit}
          measurement={{
            value: SafeParser.toFixed(metrics[METRIC_INTERNAL_CODES.PULSE]?.value),
          }}
          measureFailed={technicalAlerts.PULSE}
          isError={
            !hasActivePatientSession ||
            technicalAlerts.PULSE ||
            checkMetricSensorCharging(activeSensors, sensorMetrics, METRIC_INTERNAL_CODES.PULSE) ||
            metrics[METRIC_INTERNAL_CODES.PULSE]?.value === null
          }
        />
        <BloodPressure
          unit={
            (metrics[METRIC_INTERNAL_CODES.DIA]?.unit ||
              metrics[METRIC_INTERNAL_CODES.SYS]?.unit) as BloodPressureUnit
          }
          alertPriority={vitalsAlertSeverities[METRIC_INTERNAL_CODES.NIBP]}
          isConnected={sensorsConnected[METRIC_INTERNAL_CODES.NIBP]}
          timestamp={
            metrics[METRIC_INTERNAL_CODES.SYS]?.timestamp ||
            metrics[METRIC_INTERNAL_CODES.DIA]?.timestamp
          }
          isLoading={isLoading}
          measureFailed={technicalAlerts.NIBP}
          systolicError={
            !hasActivePatientSession ||
            technicalAlerts.NIBP ||
            checkMetricSensorCharging(activeSensors, sensorMetrics, METRIC_INTERNAL_CODES.NIBP) ||
            metrics[METRIC_INTERNAL_CODES.SYS]?.value === null
          }
          diastolicError={
            !hasActivePatientSession ||
            technicalAlerts.NIBP ||
            checkMetricSensorCharging(activeSensors, sensorMetrics, METRIC_INTERNAL_CODES.NIBP) ||
            metrics[METRIC_INTERNAL_CODES.DIA]?.value === null
          }
          systolicMeasurement={{
            value: SafeParser.toFixed(metrics[METRIC_INTERNAL_CODES.SYS]?.value),
            upperLimit: sysUpperLimit,
            lowerLimit: sysLowerLimit,
          }}
          diastolicMeasurement={{
            value: SafeParser.toFixed(metrics[METRIC_INTERNAL_CODES.DIA]?.value),
            upperLimit: diaUpperLimit,
            lowerLimit: diaLowerLimit,
          }}
          mapMeasurement={SafeParser.toFixed(metrics[METRIC_INTERNAL_CODES.MAP]?.value)}
          mapError={
            !hasActivePatientSession ||
            technicalAlerts.NIBP ||
            checkMetricSensorCharging(activeSensors, sensorMetrics, METRIC_INTERNAL_CODES.NIBP) ||
            metrics[METRIC_INTERNAL_CODES.MAP]?.value === null
          }
        />
        <BodyTemperature
          alertPriority={vitalsAlertSeverities[METRIC_INTERNAL_CODES.BODY_TEMP]}
          unit={
            (metrics[METRIC_INTERNAL_CODES.BODY_TEMP]?.unit ||
              metrics[METRIC_INTERNAL_CODES.CHEST_TEMP]?.unit ||
              metrics[METRIC_INTERNAL_CODES.LIMB_TEMP]?.unit) as TemperatureUnit
          }
          timestamp={metrics[METRIC_INTERNAL_CODES.BODY_TEMP]?.timestamp}
          isLoading={isLoading}
          isConnected={sensorsConnected[METRIC_INTERNAL_CODES.BODY_TEMP]}
          isError={
            !hasActivePatientSession ||
            technicalAlerts.BODY_TEMP ||
            checkMetricSensorCharging(
              activeSensors,
              sensorMetrics,
              METRIC_INTERNAL_CODES.BODY_TEMP
            ) ||
            metrics[METRIC_INTERNAL_CODES.BODY_TEMP]?.value === null
          }
          measurement={{
            value: SafeParser.toFixed(metrics[METRIC_INTERNAL_CODES.BODY_TEMP]?.value, 1),
            upperLimit: bodyTempUpperLimit,
            lowerLimit: bodyTempLowerLimit,
          }}
        />
        <ChestTemperature
          alertPriority={vitalsAlertSeverities[METRIC_INTERNAL_CODES.CHEST_TEMP]}
          unit={
            (metrics[METRIC_INTERNAL_CODES.CHEST_TEMP]?.unit ||
              metrics[METRIC_INTERNAL_CODES.LIMB_TEMP]?.unit ||
              metrics[METRIC_INTERNAL_CODES.BODY_TEMP]?.unit) as TemperatureUnit
          }
          isConnected={sensorsConnected[METRIC_INTERNAL_CODES.CHEST_TEMP]}
          isLoading={isLoading}
          isError={
            !hasActivePatientSession ||
            technicalAlerts.CHEST_TEMP ||
            checkMetricSensorCharging(
              activeSensors,
              sensorMetrics,
              METRIC_INTERNAL_CODES.CHEST_TEMP
            ) ||
            metrics[METRIC_INTERNAL_CODES.CHEST_TEMP]?.value === null
          }
          measurement={{
            value: SafeParser.toFixed(metrics[METRIC_INTERNAL_CODES.CHEST_TEMP]?.value, 1),
            upperLimit: skinTempUpperLimit,
            lowerLimit: skinTempLowerLimit,
          }}
        />
        <LimbTemperature
          isConnected={sensorsConnected[METRIC_INTERNAL_CODES.LIMB_TEMP]}
          alertPriority={vitalsAlertSeverities[METRIC_INTERNAL_CODES.LIMB_TEMP]}
          isLoading={isLoading}
          isError={
            !hasActivePatientSession ||
            technicalAlerts.LIMB_TEMP ||
            checkMetricSensorCharging(
              activeSensors,
              sensorMetrics,
              METRIC_INTERNAL_CODES.LIMB_TEMP
            ) ||
            metrics[METRIC_INTERNAL_CODES.LIMB_TEMP]?.value === null
          }
          measurement={{
            value: SafeParser.toFixed(metrics[METRIC_INTERNAL_CODES.LIMB_TEMP]?.value, 1),
            upperLimit: skinTempUpperLimit,
            lowerLimit: skinTempLowerLimit,
          }}
        />
      </Grid>
      <Grid display='flex' flex={1} flexDirection='column' justifyContent='space-between' gap={8}>
        <FallDetector
          state={fallState}
          alertPriority={vitalsAlertSeverities[METRIC_INTERNAL_CODES.FALLS]}
          isLoading={
            isLoading ||
            (sensorsConnected[METRIC_INTERNAL_CODES.FALLS] &&
              metrics[METRIC_INTERNAL_CODES.FALLS]?.value === undefined)
          }
        />
        <BodyPosition
          position={(metrics[METRIC_INTERNAL_CODES.POSITION]?.value as POSITION_TYPES) || null}
          angle={SafeParser.toFixed(metrics[METRIC_INTERNAL_CODES.BODY_ANGLE]?.value, 0)}
          alertPriority={vitalsAlertSeverities[METRIC_INTERNAL_CODES.POSITION]}
          hoursInCurrentPosition={hoursInCurrentPosition}
          minutesInCurrentPosition={minutesInCurrentPosition}
          isConnected={sensorsConnected[METRIC_INTERNAL_CODES.POSITION]}
          isLoading={
            isLoading ||
            (sensorsConnected[METRIC_INTERNAL_CODES.POSITION] &&
              metrics[METRIC_INTERNAL_CODES.POSITION]?.value === undefined)
          }
          hasTechnicalAlert={technicalAlerts.BODY_POSITION}
          alertConditionEnabled={
            alertThresholds[RANGES_CODES.POSITION_DURATION]?.alertConditionEnabled || false
          }
        />
      </Grid>
    </Grid>
  );
};

export default VitalMetricsPanel;
