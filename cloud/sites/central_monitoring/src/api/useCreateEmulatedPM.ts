/* eslint-disable camelcase */
import { PMCreationPayload } from '@/app/emulator/page';
import { PatientGender } from '@/types/patient';
import { ServerErrorResponse } from '@/types/response';
import { SENSOR_TYPES } from '@/types/sensor';
import { emulatorClient } from '@/utils/httpClient';
import { useMutation } from '@tanstack/react-query';
import { AxiosResponse } from 'axios';
import { v4 as uuid } from 'uuid';

type CreatePMRequest = {
  primary_identifier: string;
  name: string;
  patient?: {
    primary_identifier: string;
    given_name: string;
    family_name: string;
    gender: PatientGender;
    birth_date: string;
  };
  connected_sensors: {
    primary_identifier: string;
    name: string;
    device_code: SENSOR_TYPES;
  }[];
  config: {
    audio_pause_enabled: boolean;
    audio_enabled: boolean;
  };
};

type CreatePMResponse = null;

const createEmulatedPM = async (
  data: PMCreationPayload
): Promise<AxiosResponse<CreatePMResponse>> => {
  const createPMRequest: CreatePMRequest = {
    primary_identifier: data.pmPrimaryIdentifier,
    name: data.pmName,
    patient: data.patient
      ? {
          primary_identifier: data.patient.patientPrimaryIdentifier,
          given_name: data.patient.patientGivenName,
          family_name: data.patient.patientFamilyName,
          gender: data.patient.patientGender,
          birth_date: data.patient.patientBirthDate,
        }
      : undefined,
    connected_sensors: data.sensors.map((value) => {
      const id = uuid();
      return { primary_identifier: id, name: value, device_code: value };
    }),
    config: {
      audio_pause_enabled: false,
      audio_enabled: true,
    },
  };

  return emulatorClient.post('/emulator/monitor/ConnectPatientMonitor', createPMRequest);
};

export const useCreateEmulatedPM = () => {
  const { mutateAsync, ...rest } = useMutation<
    AxiosResponse<CreatePMResponse>,
    ServerErrorResponse,
    PMCreationPayload
  >({
    mutationFn: createEmulatedPM,
    mutationKey: ['create-emulated-pm'],
  });
  return { createEmulatedPM: mutateAsync, ...rest };
};
