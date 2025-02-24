/* eslint-disable camelcase */
import { ServerErrorResponse } from '@/types/response';
import { emulatorClient } from '@/utils/httpClient';
import { useMutation } from '@tanstack/react-query';
import { AxiosResponse } from 'axios';
import { SendEmulatedAlertRequest } from './useSendEmulatedVitalAlert';

const StaticAlertFields = {
  description: 'description',
  determination_time: 0,
  vital_range: {
    code: '0001',
    upper_limit: 0,
    lower_limit: 0,
    alert_condition_enabled: true,
  },
};

type SendEmulatedTechnicalAlertResponse = null;

const sendEmulatedTechnicalAlert = async (
  request: SendEmulatedAlertRequest
): Promise<AxiosResponse<SendEmulatedTechnicalAlertResponse>> => {
  return emulatorClient.put('/emulator/technical_alert', {
    ...StaticAlertFields,
    patient_primary_identifier: request.patientPrimaryIdentifier,
    code: request.code,
    priority: request.priority,
    device_code: request.deviceCode,
    device_primary_identifier: request.devicePrimaryIdentifier,
    active: request.active,
  });
};

export const useSendEmulatedTechnicalAlert = () => {
  const { mutateAsync, ...rest } = useMutation<
    AxiosResponse<SendEmulatedTechnicalAlertResponse>,
    ServerErrorResponse,
    SendEmulatedAlertRequest
  >({
    mutationFn: sendEmulatedTechnicalAlert,
    mutationKey: ['send-emulated-technical-alert'],
  });
  return { sendEmulatedTechnicalAlert: mutateAsync, ...rest };
};
