'use client';

import { useHealthcheck } from '@/api/useHealthcheck';
import NetworkStatusModal from '@/components/modals/NetworkStatusModal';
import useAudioManager from '@/hooks/useAudioManager';
import useNetwork from '@/hooks/useNetwork';
import { generateLostConnectionAlert } from '@/utils/alertUtils';
import { useQueryClient } from '@tanstack/react-query';
import { useCallback } from 'react';
import { useTranslation } from 'react-i18next';

const NetworkManager = (): JSX.Element => {
  const queryClient = useQueryClient();
  const networkIsOnline = useNetwork();
  const serverIsOnline = useHealthcheck();
  const { setAudioAlert, setActiveAlertsExist } = useAudioManager();
  const { t } = useTranslation();

  const onLostConnection = useCallback(() => {
    setAudioAlert([generateLostConnectionAlert(networkIsOnline)], true);
    setActiveAlertsExist(true);
  }, [networkIsOnline, setAudioAlert]);

  const onConfirm = useCallback(() => {
    void queryClient.resetQueries();
  }, [queryClient]);

  return (
    <>
      <NetworkStatusModal
        isOnline={networkIsOnline}
        onLostConnection={onLostConnection}
        onConfirm={onConfirm}
        title={t('NetworkManagementModal.networkDisconnectedTitle')}
        description={t('NetworkManagementModal.networkDisconnectedDescription')}
      />
      <NetworkStatusModal
        isOnline={serverIsOnline}
        onLostConnection={onLostConnection}
        onConfirm={onConfirm}
        title={t('NetworkManagementModal.serverDisconnectedTitle')}
        description={t('NetworkManagementModal.serverDisconnectedDescription')}
      />
    </>
  );
};

export default NetworkManager;
