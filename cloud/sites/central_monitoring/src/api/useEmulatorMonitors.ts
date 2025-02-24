import { EmulatorMonitor, ServerEmulatorMonitor } from '@/types/emulator';
import { emulatorClient } from '@/utils/httpClient';
import { useQuery } from '@tanstack/react-query';
import { parseEmulatedMonitorData } from './emulatorsApi';
import { get } from 'lodash';

const getEmulatorMonitors = async (signal?: AbortSignal) => {
  const res = await emulatorClient<ServerEmulatorMonitor>('/emulator/monitor', {
    signal,
  });
  return parseEmulatedMonitorData(get(res.data, 'resources', []));
};

const emulatorMonitorsDefaultData: EmulatorMonitor[] = [];

export const useEmulatorMonitors = () => {
  const { data, ...rest } = useQuery<EmulatorMonitor[], Error>({
    queryKey: ['emulator-monitors'],
    queryFn: ({ signal }) => getEmulatorMonitors(signal),
    placeholderData: emulatorMonitorsDefaultData,
  });

  return { data: data || emulatorMonitorsDefaultData, ...rest };
};
