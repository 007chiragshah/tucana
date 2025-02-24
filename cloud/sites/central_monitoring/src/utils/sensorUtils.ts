import { BedType } from '@/types/bed';
import { Metrics } from '@/types/metrics';
import { PatientPrimaryID } from '@/types/patient';
import { PatientMonitor } from '@/types/patientMonitor';
import { Sensor } from '@/types/sensor';
import { METRIC_INTERNAL_CODES, METRIC_SENSOR_MAP, WS_CODES } from '@/utils/metricCodes';
import { get } from 'lodash';

export enum BATTERY_STATUS_VALUES {
  FULL = 'Ful',
  CHARGING = 'ChB',
  DISCHARGING = 'DisChB',
  EMPTY = 'DEB',
}

/**
 * Checks if any of the active sensors handles a specific metric
 */
export const checkSensorConnection = (
  activeSensors: Sensor[],
  metric: METRIC_INTERNAL_CODES
): boolean =>
  !!METRIC_SENSOR_MAP[metric].some((sensor) =>
    activeSensors?.map(({ type }) => type).includes(sensor)
  );

/**
 *
 */
export const checkMetricSensorCharging = (
  activeSensors: Sensor[],
  sensorMetrics: Record<string, Metrics>,
  metric: METRIC_INTERNAL_CODES
): boolean => {
  return !!METRIC_SENSOR_MAP[metric].some(
    (sensor) =>
      !!activeSensors?.find(
        ({ type, primaryIdentifier }) =>
          type === sensor &&
          (get(
            sensorMetrics,
            `[${primaryIdentifier}][${WS_CODES.DEVICE_BATTERY_STATUS}].value`,
            ''
          ) as string) === BATTERY_STATUS_VALUES.CHARGING
      )
  );
};

/**
 * Returns an association between monitors and patients by monitor id.
 * PMs are associated with patients through beds, so it uses both PMs information
 * and beds information to get the final association
 */
export const associatePatientMonitorsWithPatientPrimaryIdentifier = (
  patientMonitors: PatientMonitor[],
  beds: BedType[]
) => {
  const monitorPatientHash: Record<string, PatientPrimaryID> = {};
  patientMonitors.forEach((patientMonitor) => {
    if (patientMonitor.assignedBedId) {
      const foundBed = beds.find((bed) => bed.id === patientMonitor.assignedBedId);
      if (foundBed?.patient?.patientPrimaryIdentifier)
        monitorPatientHash[patientMonitor.id] = foundBed.patient.patientPrimaryIdentifier;
    }
  });
  return monitorPatientHash;
};

/**
 * Returns if the battery is charging or not based on the status received
 */
export const batteryStatusToBoolean = (batteryStatus?: string | null) => {
  return batteryStatus === BATTERY_STATUS_VALUES.CHARGING;
};

/**
 * Returns if the sensor metric value is valid for that particular metric
 */
export const sensorMetricIsValid = (metricCode: string, metricValue: number | string | null) => {
  if (metricCode === WS_CODES.DEVICE_BATTERY) {
    return metricValue !== null && (metricValue as number) >= 0;
  }
  return true;
};
