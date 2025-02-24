/* eslint-disable camelcase */
import { ServerErrorResponse } from '@/types/response';
import { emulatorClient } from '@/utils/httpClient';
import { useMutation } from '@tanstack/react-query';
import { AxiosResponse } from 'axios';

type DisconnectEmulatedPMResponse = null;

const disconnectEmulatedPMRequest = async (
  primaryIdentifier: string
): Promise<AxiosResponse<DisconnectEmulatedPMResponse>> => {
  return emulatorClient.post('/emulator/monitor/DisconnectMonitor', {
    primary_identifier: primaryIdentifier,
  });
};

export const useDisconnectEmulatedPM = () => {
  const { mutateAsync, ...rest } = useMutation<
    AxiosResponse<DisconnectEmulatedPMResponse>,
    ServerErrorResponse,
    string
  >({
    mutationFn: disconnectEmulatedPMRequest,
    mutationKey: ['disconnect-emulated-pm'],
  });
  return { disconnectEmulatedPM: mutateAsync, ...rest };
};
