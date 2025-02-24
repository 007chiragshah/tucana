'use client';

import { useHealthcheck } from '@/api/useHealthcheck';
import useNetwork from '@/hooks/useNetwork';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { useEffect, useState } from 'react';
import { getCachedRuntimeConfig } from '../../utils/runtime';
import NetworkErrorChip from './NetworkErrorChip';
import PatientMonitorWarning from './PatientMonitorWarning';
import { USER_TYPE } from '@/constants';
import useSession from '@/hooks/useSession';
import useTime from '@/hooks/useTime';
import { useTranslation } from 'react-i18next';

const SystemStatusBar = () => {
  const [title, setTitle] = useState<string>();
  const currentDate = useTime();
  const { userType } = useSession();
  const networkIsOnline = useNetwork();
  const serverIsOnline = useHealthcheck();
  const { t } = useTranslation();

  useEffect(() => {
    // Sets hospital name
    setTitle(getCachedRuntimeConfig().HOSPITAL_TITLE);
  }, []);

  return (
    <Grid
      container
      direction='row'
      alignItems='center'
      px={16}
      py={3}
      sx={{
        backgroundColor: 'common.black',
        height: 46,
      }}
    >
      <Grid item display='flex' flexDirection='row' flexGrow={1} alignItems='center' gap={25}>
        <Typography lineHeight='22px' textAlign='center' variant='caption'>
          {currentDate && `${currentDate.format('yyyy-MM-DD')} | ${currentDate.format('HH:mm')}`}
        </Typography>
        {userType == USER_TYPE.NON_TECH && <PatientMonitorWarning />}
      </Grid>
      <Grid item display='flex' flexDirection='row' alignItems='center' gap={5}>
        {!networkIsOnline && <NetworkErrorChip text={t('ErrorChips.networkError')} />}
        {!serverIsOnline &&
          (userType == USER_TYPE.TECH ? (
            <NetworkErrorChip text={t('ErrorChips.serverError')} />
          ) : (
            <NetworkErrorChip text={t('ErrorChips.dataError')} />
          ))}
        <Typography lineHeight='22px' variant='caption'>
          {title}
        </Typography>
      </Grid>
    </Grid>
  );
};

export default SystemStatusBar;
