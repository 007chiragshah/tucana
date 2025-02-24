import Box from '@mui/material/Box';

import Loading from '../loading';
import EmulatorModalContainer from './EmulatorModalContainer';
import {
  StyledEmulationActionButton,
  StyledEmulationSectionTitle,
} from './components/EmulatedStyledComponents';
import { EmulatorMonitor, EmulatorSensor } from '@/types/emulator';
import EmulatedAlarmConditionSection from './components/EmulatedAlarmConditionSection';
import Typography from '@mui/material/Typography';
import { ALERT_PRIORITY, ALERT_TYPES } from '@/utils/metricCodes';
import { SendEmulatedAlertRequest } from '@/api/useSendEmulatedVitalAlert';
import EmulatedPatientDisplay from './components/EmulatedPatientDisplay';
import { SENSOR_TYPES } from '@/types/sensor';

interface PMDataModalProps {
  isOpen: boolean;
  isLoading: boolean;
  pmData?: EmulatorMonitor;
  onSendVitalAlert: (payload: SendEmulatedAlertRequest) => void;
  onSendTechnicalAlert: (payload: SendEmulatedAlertRequest) => void;
  onClose: () => void;
  onDisconnect: (primaryIdentifier: string) => void;
}

const PMDataModal = ({
  isOpen,
  onClose,
  pmData,
  onSendVitalAlert,
  onSendTechnicalAlert,
  isLoading,
  onDisconnect,
}: PMDataModalProps) => {
  const handleSendVitalAlert = (
    sensorId: string,
    sensorType: SENSOR_TYPES,
    alarmCode: string,
    alarmPriority: ALERT_PRIORITY,
    active: boolean
  ) => {
    if (pmData?.patient) {
      onSendVitalAlert({
        patientPrimaryIdentifier: pmData.patient.primaryIdentifier,
        code: alarmCode,
        priority: alarmPriority,
        deviceCode: sensorType,
        devicePrimaryIdentifier: sensorId,
        active,
      });
    }
  };

  const handleSendTechnicalAlert = (
    sensorId: string,
    sensorType: SENSOR_TYPES,
    alarmCode: string,
    alarmPriority: ALERT_PRIORITY,
    active: boolean
  ) => {
    if (pmData?.patient) {
      onSendTechnicalAlert({
        patientPrimaryIdentifier: pmData.patient.primaryIdentifier,
        code: alarmCode,
        priority: alarmPriority,
        deviceCode: sensorType,
        devicePrimaryIdentifier: sensorId,
        active,
      });
    }
  };

  if (!pmData) {
    return null;
  }
  return (
    <EmulatorModalContainer
      modalHidden={!isOpen}
      onClose={onClose}
      headerTitle={`PM Information (${pmData.primaryIdentifier})`}
    >
      {isLoading ? (
        <Box display='flex' width='100%' height='100%' alignContent='center' flexWrap='wrap'>
          <Loading height={64} />
        </Box>
      ) : (
        <Box
          display='flex'
          flexDirection='column'
          sx={{ overflow: 'scroll', width: '100%', gap: '15px' }}
        >
          <StyledEmulationSectionTitle>Associated Patient</StyledEmulationSectionTitle>
          <EmulatedPatientDisplay patient={pmData.patient} />
          <StyledEmulationSectionTitle>Connected Sensors</StyledEmulationSectionTitle>
          <Box sx={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-between' }}>
            {pmData.sensors.map((sensor: EmulatorSensor) => {
              return (
                <Box
                  key={`emulated_sensor_${sensor.primaryIdentifier}`}
                  sx={{ display: 'flex', flexDirection: 'row' }}
                >
                  <Typography variant='h6' sx={{ alignSelf: 'center' }}>
                    {sensor.type}
                  </Typography>
                </Box>
              );
            })}
          </Box>
          <EmulatedAlarmConditionSection
            title='VITALS ALERTS (Only available if PM has an associated patient)'
            instructions='First pick a sensor from the dropdown. Then select the alert you wish to send. Finally click either Send to activate the alert or Remove to disable it'
            alertType={ALERT_TYPES.VITALS}
            sensors={pmData.sensors}
            onSubmit={(
              sensorId: string,
              sensorType: SENSOR_TYPES,
              alarmCode: string,
              alarmPriority: ALERT_PRIORITY,
              active: boolean
            ) => {
              handleSendVitalAlert(sensorId, sensorType, alarmCode, alarmPriority, active);
            }}
          />
          <EmulatedAlarmConditionSection
            title='TECHNICAL ALERTS'
            instructions='First pick a sensor from the dropdown. Then select the alert you wish to send. Finally click either Send to activate the alert or Remove to disable it'
            alertType={ALERT_TYPES.DEVICE}
            sensors={pmData.sensors}
            onSubmit={(
              sensorId: string,
              sensorType: SENSOR_TYPES,
              alarmCode: string,
              alarmPriority: ALERT_PRIORITY,
              active: boolean
            ) => {
              handleSendTechnicalAlert(sensorId, sensorType, alarmCode, alarmPriority, active);
            }}
          />
          <StyledEmulationActionButton
            onClick={() => onDisconnect(pmData.primaryIdentifier)}
            sx={{ color: 'red', borderColor: 'red' }}
          >
            Disconnect PM (IRREVERSIBLE!)
          </StyledEmulationActionButton>
        </Box>
      )}
    </EmulatorModalContainer>
  );
};

export default PMDataModal;
