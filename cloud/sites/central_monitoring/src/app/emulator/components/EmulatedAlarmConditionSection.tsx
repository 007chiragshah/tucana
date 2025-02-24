import { EmulatorSensor } from '@/types/emulator';
import {
  StyledEmulationActionButton,
  StyledEmulationMenuItem,
  StyledEmulationSectionSubtitle,
  StyledEmulationSectionTitle,
} from './EmulatedStyledComponents';
import Box from '@mui/material/Box';
import { ReactNode, useMemo, useState } from 'react';
import {
  ALERT_PRIORITY,
  ALERT_TYPES,
  DEVICE_ALERT_CODES,
  VITALS_ALERT_CODES,
} from '@/utils/metricCodes';
import { SENSOR_TYPES } from '@/types/sensor';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import { AlertMetadata } from '@/types/alerts';

interface EmulatedAlarmConditionSectionProps {
  title: string;
  instructions: string;
  alertType: ALERT_TYPES;
  sensors: EmulatorSensor[];
  onSubmit: (
    sensorId: string,
    sensorType: SENSOR_TYPES,
    alertCode: string,
    alarmPriority: ALERT_PRIORITY,
    active: boolean
  ) => void;
}

type ALERT_GROUPING = {
  key: string;
  display: string;
  codes: string[];
};

const VITAL_ALERTS_GROUPINGS: Record<string, ALERT_GROUPING> = {
  HR_HIGH: {
    key: 'HR_HIGH',
    display: 'HR HIGH',
    codes: [VITALS_ALERT_CODES.HR_HIGH_VISUAL.code, VITALS_ALERT_CODES.HR_HIGH_AUDIO.code],
  },
  HR_LOW: {
    key: 'HR_LOW',
    display: 'HR LOW',
    codes: [VITALS_ALERT_CODES.HR_LOW_VISUAL.code, VITALS_ALERT_CODES.HR_LOW_AUDIO.code],
  },
  RR_HIGH: {
    key: 'RR_HIGH',
    display: 'RR HIGH',
    codes: [VITALS_ALERT_CODES.RR_HIGH_VISUAL.code, VITALS_ALERT_CODES.RR_HIGH_AUDIO.code],
  },
  RR_LOW: {
    key: 'RR_LOW',
    display: 'RR LOW',
    codes: [VITALS_ALERT_CODES.RR_LOW_VISUAL.code, VITALS_ALERT_CODES.RR_LOW_AUDIO.code],
  },
  SPO2_HIGH: {
    key: 'SPO2_HIGH',
    display: 'SPO2 HIGH',
    codes: [VITALS_ALERT_CODES.SPO2_HIGH_VISUAL.code, VITALS_ALERT_CODES.SPO2_HIGH_AUDIO.code],
  },
  SPO2_LOW: {
    key: 'SPO2_LOW',
    display: 'SPO2 LOW',
    codes: [VITALS_ALERT_CODES.SPO2_LOW_VISUAL.code, VITALS_ALERT_CODES.SPO2_LOW_AUDIO.code],
  },
  PR_HIGH: {
    key: 'PR_HIGH',
    display: 'PR HIGH',
    codes: [VITALS_ALERT_CODES.PR_HIGH_VISUAL.code, VITALS_ALERT_CODES.PR_HIGH_AUDIO.code],
  },
  PR_LOW: {
    key: 'PR_LOW',
    display: 'PR LOW',
    codes: [VITALS_ALERT_CODES.PR_LOW_VISUAL.code, VITALS_ALERT_CODES.PR_LOW_AUDIO.code],
  },
  SYS_HIGH: {
    key: 'SYS_HIGH',
    display: 'SYS HIGH',
    codes: [VITALS_ALERT_CODES.SYS_HIGH_VISUAL.code, VITALS_ALERT_CODES.SYS_HIGH_AUDIO.code],
  },
  SYS_LOW: {
    key: 'SYS_LOW',
    display: 'SYS LOW',
    codes: [VITALS_ALERT_CODES.SYS_LOW_VISUAL.code, VITALS_ALERT_CODES.SYS_LOW_AUDIO.code],
  },
  DIA_HIGH: {
    key: 'DIA_HIGH',
    display: 'DIA HIGH',
    codes: [VITALS_ALERT_CODES.DIA_HIGH_VISUAL.code, VITALS_ALERT_CODES.DIA_HIGH_AUDIO.code],
  },
  DIA_LOW: {
    key: 'DIA_LOW',
    display: 'DIA LOW',
    codes: [VITALS_ALERT_CODES.DIA_LOW_VISUAL.code, VITALS_ALERT_CODES.DIA_LOW_AUDIO.code],
  },
  BODY_TEMP_HIGH: {
    key: 'BODY_TEMP_HIGH',
    display: 'BODY TEMP HIGH',
    codes: [
      VITALS_ALERT_CODES.BODY_TEMP_HIGH_VISUAL.code,
      VITALS_ALERT_CODES.BODY_TEMP_HIGH_AUDIO.code,
    ],
  },
  BODY_TEMP_LOW: {
    key: 'BODY_TEMP_LOW',
    display: 'BODY TEMP LOW',
    codes: [
      VITALS_ALERT_CODES.BODY_TEMP_LOW_VISUAL.code,
      VITALS_ALERT_CODES.BODY_TEMP_LOW_AUDIO.code,
    ],
  },
  CHEST_TEMP_HIGH: {
    key: 'CHEST_TEMP_HIGH',
    display: 'CHEST TEMP HIGH',
    codes: [
      VITALS_ALERT_CODES.CHEST_TEMP_HIGH_VISUAL.code,
      VITALS_ALERT_CODES.CHEST_TEMP_HIGH_AUDIO.code,
    ],
  },
  CHEST_TEMP_LOW: {
    key: 'CHEST_TEMP_LOW',
    display: 'CHEST TEMP LOW',
    codes: [
      VITALS_ALERT_CODES.CHEST_TEMP_LOW_VISUAL.code,
      VITALS_ALERT_CODES.CHEST_TEMP_LOW_AUDIO.code,
    ],
  },
  LIMB_TEMP_HIGH: {
    key: 'LIMB_TEMP_HIGH',
    display: 'LIMB TEMP HIGH',
    codes: [
      VITALS_ALERT_CODES.LIMB_TEMP_HIGH_VISUAL.code,
      VITALS_ALERT_CODES.LIMB_TEMP_HIGH_AUDIO.code,
    ],
  },
  LIMB_TEMP_LOW: {
    key: 'LIMB_TEMP_LOW',
    display: 'LIMB TEMP LOW',
    codes: [
      VITALS_ALERT_CODES.LIMB_TEMP_LOW_VISUAL.code,
      VITALS_ALERT_CODES.LIMB_TEMP_LOW_AUDIO.code,
    ],
  },
  FALL: {
    key: 'FALL',
    display: 'FALL',
    codes: [VITALS_ALERT_CODES.FALL_VISUAL.code, VITALS_ALERT_CODES.FALL_AUDIO.code],
  },
  POSITION: {
    key: 'POSITION',
    display: 'POSITION',
    codes: [VITALS_ALERT_CODES.POSITION_VISUAL.code, VITALS_ALERT_CODES.POSITION_AUDIO.code],
  },
};

const VITAL_ALERTS_PER_MONITOR: Partial<Record<SENSOR_TYPES, ALERT_GROUPING[]>> = {
  [SENSOR_TYPES.CHEST]: [
    VITAL_ALERTS_GROUPINGS.HR_HIGH,
    VITAL_ALERTS_GROUPINGS.HR_LOW,
    VITAL_ALERTS_GROUPINGS.CHEST_TEMP_HIGH,
    VITAL_ALERTS_GROUPINGS.CHEST_TEMP_LOW,
    VITAL_ALERTS_GROUPINGS.FALL,
    VITAL_ALERTS_GROUPINGS.RR_HIGH,
    VITAL_ALERTS_GROUPINGS.RR_LOW,
    VITAL_ALERTS_GROUPINGS.POSITION,
  ],
  [SENSOR_TYPES.LIMB]: [
    VITAL_ALERTS_GROUPINGS.SPO2_HIGH,
    VITAL_ALERTS_GROUPINGS.SPO2_LOW,
    VITAL_ALERTS_GROUPINGS.PR_HIGH,
    VITAL_ALERTS_GROUPINGS.PR_LOW,
    VITAL_ALERTS_GROUPINGS.LIMB_TEMP_HIGH,
    VITAL_ALERTS_GROUPINGS.LIMB_TEMP_LOW,
  ],
  [SENSOR_TYPES.NONIN]: [
    VITAL_ALERTS_GROUPINGS.SPO2_HIGH,
    VITAL_ALERTS_GROUPINGS.SPO2_LOW,
    VITAL_ALERTS_GROUPINGS.PR_HIGH,
    VITAL_ALERTS_GROUPINGS.PR_LOW,
  ],
  [SENSOR_TYPES.THERMOMETER]: [
    VITAL_ALERTS_GROUPINGS.BODY_TEMP_HIGH,
    VITAL_ALERTS_GROUPINGS.BODY_TEMP_LOW,
  ],
  [SENSOR_TYPES.BP]: [
    VITAL_ALERTS_GROUPINGS.SYS_HIGH,
    VITAL_ALERTS_GROUPINGS.SYS_LOW,
    VITAL_ALERTS_GROUPINGS.DIA_HIGH,
    VITAL_ALERTS_GROUPINGS.DIA_LOW,
  ],
};

const TECNICAL_ALERTS_PER_MONITOR: Partial<Record<SENSOR_TYPES, AlertMetadata[]>> = {
  [SENSOR_TYPES.CHEST]: [
    DEVICE_ALERT_CODES.LEAD_OFF_ALERT,
    DEVICE_ALERT_CODES.MODULE_FAILURE_ALERT,
    DEVICE_ALERT_CODES.LOW_BATTERY_ALERT,
    DEVICE_ALERT_CODES.CRITICAL_BATTERY_ALERT,
    DEVICE_ALERT_CODES.LOW_SIGNAL_ALERT,
    DEVICE_ALERT_CODES.OUT_OF_RANGE_ALERT,
  ],
  [SENSOR_TYPES.LIMB]: [
    DEVICE_ALERT_CODES.POOR_SKIN_CONTACT_ALERT,
    DEVICE_ALERT_CODES.MODULE_FAILURE_ALERT,
    DEVICE_ALERT_CODES.LOW_BATTERY_ALERT,
    DEVICE_ALERT_CODES.CRITICAL_BATTERY_ALERT,
    DEVICE_ALERT_CODES.LOW_SIGNAL_ALERT,
    DEVICE_ALERT_CODES.OUT_OF_RANGE_ALERT,
  ],
  [SENSOR_TYPES.NONIN]: [
    DEVICE_ALERT_CODES.FINGER_NOT_DETECTED_ALERT,
    DEVICE_ALERT_CODES.MODULE_FAILURE_ALERT,
    DEVICE_ALERT_CODES.SYSTEM_ERROR_ALERT,
    DEVICE_ALERT_CODES.OUT_OF_RANGE_ALERT,
  ],
  [SENSOR_TYPES.BP]: [
    DEVICE_ALERT_CODES.LOOSE_SLEEVE_ALERT,
    DEVICE_ALERT_CODES.MOVEMENT_DETECTED_ALERT,
    DEVICE_ALERT_CODES.WEAK_PULSE_ALERT,
    DEVICE_ALERT_CODES.MODULE_FAILURE_ALERT,
  ],
};

const EmulatedAlarmConditionSection = ({
  title,
  instructions,
  alertType,
  sensors,
  onSubmit,
}: EmulatedAlarmConditionSectionProps) => {
  const [selectedSensor, setSelectedSensor] = useState<EmulatorSensor | null>(null);
  const [selectedAlert, setSelectedAlert] = useState<string>('');
  const [selectedPriority, setSelectedPriority] = useState<ALERT_PRIORITY>(ALERT_PRIORITY.HIGH);

  const renderedSensors = useMemo(() => {
    const res: ReactNode[] = [];
    sensors.forEach((sensor) => {
      if (alertType !== ALERT_TYPES.DEVICE || sensor.type !== SENSOR_TYPES.THERMOMETER) {
        res.push(
          <StyledEmulationMenuItem
            value={sensor.type}
            key={`sensor_option_${sensor.primaryIdentifier}`}
          >
            {sensor.type}
          </StyledEmulationMenuItem>
        );
      }
    });
    return res;
  }, [alertType, sensors]);

  const renderedAlerts = useMemo(() => {
    const res: ReactNode[] = [];
    if (selectedSensor) {
      if (alertType === ALERT_TYPES.VITALS) {
        (VITAL_ALERTS_PER_MONITOR[selectedSensor.type] || []).forEach(({ key, display }) => {
          res.push(
            <StyledEmulationMenuItem value={key} key={`alert_option_${key}`}>
              {display}
            </StyledEmulationMenuItem>
          );
        });
      } else {
        (TECNICAL_ALERTS_PER_MONITOR[selectedSensor.type] || []).forEach((data: AlertMetadata) => {
          res.push(
            <StyledEmulationMenuItem value={data.code} key={`alert_option_${data.code}`}>
              {data.message}
            </StyledEmulationMenuItem>
          );
        });
      }
    }
    return res;
  }, [alertType, selectedSensor]);

  const handleSubmit = (active: boolean) => {
    if (selectedSensor && selectedAlert) {
      if (alertType === ALERT_TYPES.VITALS) {
        VITAL_ALERTS_GROUPINGS[selectedAlert].codes.forEach((alertCode) => {
          onSubmit(
            selectedSensor.primaryIdentifier,
            selectedSensor.type,
            alertCode,
            selectedPriority,
            active
          );
        });
      } else {
        onSubmit(
          selectedSensor.primaryIdentifier,
          selectedSensor.type,
          selectedAlert,
          selectedPriority,
          active
        );
      }
    }
  };

  return (
    <Box>
      <StyledEmulationSectionTitle>{title}</StyledEmulationSectionTitle>
      <StyledEmulationSectionSubtitle>{instructions}</StyledEmulationSectionSubtitle>
      <Box sx={{ flexDirection: 'row', display: 'flex', gap: '25px' }}>
        <FormControl fullWidth variant='outlined' sx={{ borderRadius: 16, mt: '15px', flex: 3 }}>
          <InputLabel id='selectSensorLabel'>Select Sensor</InputLabel>
          <Select
            id='selectedSensor'
            labelId='selectedSensorLabel'
            value={selectedSensor?.type || ''}
            fullWidth
            onChange={(e) => {
              const selectedSensorType = e.target.value;
              const newSelectedSensor =
                sensors.find((sensor) => sensor.type === selectedSensorType) || null;
              setSelectedSensor(newSelectedSensor);
            }}
            label='Select Sensor'
          >
            {renderedSensors}
          </Select>
        </FormControl>
        <FormControl
          fullWidth
          variant='outlined'
          sx={{ borderRadius: 16, mt: '15px', mb: '15px', flex: 3 }}
        >
          <InputLabel id='selectAlertLabel'>Select Alert</InputLabel>
          <Select
            id='selectedAlert'
            labelId='selectedAlertLabel'
            value={selectedAlert}
            fullWidth
            onChange={(e) => {
              setSelectedAlert(e.target.value);
            }}
            label='Select Alert'
            disabled={!selectedSensor}
          >
            {renderedAlerts}
          </Select>
        </FormControl>
        <FormControl
          fullWidth
          variant='outlined'
          sx={{ borderRadius: 16, mt: '15px', mb: '15px', flex: 1 }}
        >
          <InputLabel id='selectedPriorityLabel'>Select Priority</InputLabel>
          <Select
            id='selectedPriority'
            labelId='selectedPriorityLabel'
            value={selectedPriority}
            fullWidth
            onChange={(e) => {
              setSelectedPriority(e.target.value as ALERT_PRIORITY);
            }}
            label='Select Priority'
          >
            <StyledEmulationMenuItem value={ALERT_PRIORITY.HIGH}>High</StyledEmulationMenuItem>
            <StyledEmulationMenuItem value={ALERT_PRIORITY.MEDIUM}>Medium</StyledEmulationMenuItem>
            <StyledEmulationMenuItem value={ALERT_PRIORITY.LOW}>Low</StyledEmulationMenuItem>
          </Select>
        </FormControl>
      </Box>
      <Box
        sx={{
          width: '100%',
          flexDirection: 'row',
          display: 'flex',
          justifyContent: 'center',
          gap: '25px',
        }}
      >
        <StyledEmulationActionButton
          onClick={() => handleSubmit(true)}
          disabled={!selectedSensor || !selectedAlert || !selectedPriority}
        >
          Send
        </StyledEmulationActionButton>
        <StyledEmulationActionButton
          onClick={() => handleSubmit(false)}
          disabled={!selectedSensor || !selectedAlert || !selectedPriority}
        >
          Remove
        </StyledEmulationActionButton>
      </Box>
    </Box>
  );
};

export default EmulatedAlarmConditionSection;
