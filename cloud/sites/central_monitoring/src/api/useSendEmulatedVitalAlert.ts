/* eslint-disable camelcase */
import { ServerErrorResponse } from '@/types/response';
import { SENSOR_TYPES } from '@/types/sensor';
import { emulatorClient } from '@/utils/httpClient';
import { ALERT_PRIORITY } from '@/utils/metricCodes';
import { useMutation } from '@tanstack/react-query';
import { AxiosResponse } from 'axios';

export type SendEmulatedAlertRequest = {
  patientPrimaryIdentifier: string;
  code: string;
  priority: ALERT_PRIORITY;
  deviceCode: SENSOR_TYPES;
  devicePrimaryIdentifier: string;
  active: boolean;
};

const StaticAlertFields = {
  description: 'description',
  determination_time: 0,
  vital_range: {
    code: '0001',
    upper_limit: 0,
    lower_limit: 0,
    alert_condition_enabled: true,
  },
  latching: false,
};

type SendEmulatedVitalAlertResponse = null;

const sendEmulatedVitalAlert = async (
  request: SendEmulatedAlertRequest
): Promise<AxiosResponse<SendEmulatedVitalAlertResponse>> => {
  return emulatorClient.put('/emulator/alarm', {
    ...StaticAlertFields,
    patient_primary_identifier: request.patientPrimaryIdentifier,
    code: request.code,
    priority: request.priority,
    device_code: request.deviceCode,
    device_primary_identifier: request.devicePrimaryIdentifier,
    active: request.active,
  });
};

export const useSendEmulatedVitalAlert = () => {
  const { mutateAsync, ...rest } = useMutation<
    AxiosResponse<SendEmulatedVitalAlertResponse>,
    ServerErrorResponse,
    SendEmulatedAlertRequest
  >({
    mutationFn: sendEmulatedVitalAlert,
    mutationKey: ['send-emulated-vital-alert'],
  });
  return { sendEmulatedVitalAlert: mutateAsync, ...rest };
};
