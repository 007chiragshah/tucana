import Box from '@mui/material/Box';
import { useMemo, useState } from 'react';

import Loading from '../loading';
import { SENSOR_TYPES } from '@/types/sensor';
import { PatientGender } from '@/types/patient';
import Typography from '@mui/material/Typography';
import Select from '@mui/material/Select';
import { PMCreationPayload } from './page';
import Checkbox from '@mui/material/Checkbox';
import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';
import EmulatorModalContainer from './EmulatorModalContainer';
import {
  StyledEmulationActionButton,
  StyledEmulationMenuItem,
  StyledEmulationSectionTitle,
  StyledEmulationTextField,
} from './components/EmulatedStyledComponents';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import moment from 'moment';

interface CreatePMModalProps {
  isOpen: boolean;
  onClose: () => void;
  isLoading: boolean;
  onSave: (payload: PMCreationPayload) => void;
}

const SensorOptions: SENSOR_TYPES[] = [
  SENSOR_TYPES.CHEST,
  SENSOR_TYPES.LIMB,
  SENSOR_TYPES.BP,
  SENSOR_TYPES.NONIN,
  SENSOR_TYPES.THERMOMETER,
];

const DATE_FORMAT = 'YYYY-MM-DD';
const UNALLOWED_PAIRS = [[SENSOR_TYPES.LIMB, SENSOR_TYPES.NONIN]];

const CreatePMModal = ({ isOpen, onClose, isLoading, onSave }: CreatePMModalProps) => {
  const [pmPrimaryIdentifier, setPMPrimaryIdentifier] = useState<string>('');
  const [pmName, setPMName] = useState<string>('');

  const [patientPrimaryIdentifier, setPatientPrimaryIdentifier] = useState<string>('');
  const [patientGivenName, setPatientGivenName] = useState<string>('');
  const [patientFamilyName, setPatientFamilyName] = useState<string>('');
  const [patientGender, setPatientGender] = useState<PatientGender | ''>('');
  const [patientBirthDate, setPatientBirthDate] = useState<string>('');

  const [selectedSensors, setSelectedSensors] = useState<SENSOR_TYPES[]>([]);

  const isPatientDataValid: boolean = useMemo(() => {
    const patientFields = [
      patientPrimaryIdentifier,
      patientGivenName,
      patientFamilyName,
      patientGender,
      patientBirthDate,
    ];

    return patientFields.every((v) => !v) || patientFields.every((v) => !!v);
  }, [
    patientPrimaryIdentifier,
    patientGivenName,
    patientFamilyName,
    patientGender,
    patientBirthDate,
  ]);

  const isSaveEnabled: boolean = useMemo(
    () => !!pmPrimaryIdentifier && !!pmName && isPatientDataValid,
    [pmPrimaryIdentifier, pmName, isPatientDataValid]
  );

  const unallowedSensors: SENSOR_TYPES[] = useMemo(() => {
    const res: SENSOR_TYPES[] = [];
    UNALLOWED_PAIRS.forEach(([first, second]) => {
      if (selectedSensors.includes(first) && !selectedSensors.includes(second)) {
        res.push(second);
      } else if (selectedSensors.includes(second) && !selectedSensors.includes(first)) {
        res.push(first);
      }
    });
    return res;
  }, [selectedSensors]);

  const handleSelectSensor = (isSelected: boolean, sensorType: SENSOR_TYPES) => {
    if (isSelected) {
      setSelectedSensors((previousValue) => {
        if (previousValue.includes(sensorType)) return previousValue;
        return [...previousValue, sensorType];
      });
    } else {
      setSelectedSensors((previousValue) => {
        const index = previousValue.indexOf(sensorType);
        if (index < 0) return previousValue;

        const newValues = [...previousValue];
        newValues.splice(index, 1);
        return newValues;
      });
    }
  };

  const resetValues = () => {
    setPMPrimaryIdentifier('');
    setPMName('');
    setPatientPrimaryIdentifier('');
    setPatientGivenName('');
    setPatientFamilyName('');
    setPatientGender('');
    setPatientBirthDate('');
    setSelectedSensors([]);
  };

  const handleSave = () => {
    resetValues();
    onSave({
      pmPrimaryIdentifier,
      pmName,
      patient:
        isPatientDataValid && patientPrimaryIdentifier
          ? {
              patientPrimaryIdentifier,
              patientGivenName,
              patientFamilyName,
              patientGender: patientGender as PatientGender,
              patientBirthDate,
            }
          : undefined,
      sensors: selectedSensors,
    });
  };

  const handleClose = () => {
    resetValues();
    onClose();
  };

  return (
    <EmulatorModalContainer modalHidden={!isOpen} onClose={handleClose} headerTitle='Add new PM'>
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
          <StyledEmulationSectionTitle>PM Information (required)</StyledEmulationSectionTitle>
          <StyledEmulationTextField
            label='PM Primary Identifier'
            id='pmPrimaryIdentifier'
            value={pmPrimaryIdentifier}
            onChange={(e) => {
              setPMPrimaryIdentifier(e.currentTarget.value.trim());
            }}
          />
          <StyledEmulationTextField
            fullWidth
            label='PM Name'
            id='pmName'
            value={pmName}
            onChange={(e) => {
              setPMName(e.currentTarget.value.trim());
            }}
          />
          <StyledEmulationSectionTitle>
            Patient Information (leave all empty if no patient is required)
          </StyledEmulationSectionTitle>
          <StyledEmulationTextField
            fullWidth
            label='Patient Primary Identifier'
            id='patientPrimaryIdentifier'
            value={patientPrimaryIdentifier}
            onChange={(e) => {
              setPatientPrimaryIdentifier(e.currentTarget.value.trim());
            }}
          />
          <StyledEmulationTextField
            fullWidth
            label='Patient Given Name'
            id='patientGivenName'
            value={patientGivenName}
            onChange={(e) => {
              setPatientGivenName(e.currentTarget.value.trim());
            }}
          />
          <StyledEmulationTextField
            fullWidth
            label='Patient Family Name'
            id='patientFamilyName'
            value={patientFamilyName}
            onChange={(e) => {
              setPatientFamilyName(e.currentTarget.value.trim());
            }}
            inputProps={{ style: { border: 'none' } }}
          />
          <FormControl fullWidth variant='outlined' sx={{ borderRadius: 16 }}>
            <InputLabel id='patientGenderLabel'>Patient Gender</InputLabel>
            <Select
              id='patientGender'
              labelId='patientGenderLabel'
              value={patientGender}
              fullWidth
              onChange={(e) => {
                setPatientGender(e.target.value as PatientGender);
              }}
              label='Patient Gender'
              sx={{
                border: 'none',
                borderRadius: 16,
                '&.MuiOutlinedInput-root': {
                  '& fieldset': {
                    border: 0,
                  },
                  '&:hover fieldset': {
                    border: 0,
                  },
                  '&.Mui-focused fieldset': {
                    border: 0,
                  },
                },
              }}
              MenuProps={{
                anchorOrigin: { vertical: 'top', horizontal: 'left' },
                transformOrigin: { vertical: 'top', horizontal: 'left' },
                PaperProps: {
                  sx: {
                    backgroundImage: 'none',
                    backgroundColor: 'transparent',
                  },
                },
                MenuListProps: {
                  sx: {
                    backgroundColor: 'primary.dark',
                    border: (theme) => `1px solid ${theme.palette.grey[600]}`,
                    borderRadius: 16,
                    overflow: 'hidden',
                  },
                },
              }}
            >
              <StyledEmulationMenuItem value={PatientGender.MALE}>Male</StyledEmulationMenuItem>
              <StyledEmulationMenuItem value={PatientGender.FEMALE}>Female</StyledEmulationMenuItem>
              <StyledEmulationMenuItem value={PatientGender.OTHER}>Other</StyledEmulationMenuItem>
              <StyledEmulationMenuItem value={PatientGender.UNKNOWN}>
                Unknown
              </StyledEmulationMenuItem>
            </Select>
          </FormControl>
          <DatePicker
            format={DATE_FORMAT}
            disableFuture
            closeOnSelect
            disableHighlightToday
            label='Patient Birthdate'
            className='ehrDatePicker'
            value={patientBirthDate ? moment(patientBirthDate) : null}
            onChange={(newDate) => {
              setPatientBirthDate(newDate?.format(DATE_FORMAT) || '');
            }}
          />
          <StyledEmulationSectionTitle>
            Choose Selected Sensors (only available if patient is added)
          </StyledEmulationSectionTitle>
          <Box sx={{ display: 'flex', flexDirection: 'row' }}>
            {SensorOptions.map((sensorType: SENSOR_TYPES) => {
              return (
                <Box key={`option_${sensorType}`} sx={{ display: 'flex', flexDirection: 'row' }}>
                  <Checkbox
                    checked={selectedSensors.indexOf(sensorType) >= 0}
                    onChange={(e) => {
                      handleSelectSensor(e.target.checked, sensorType);
                    }}
                    disabled={
                      !isPatientDataValid ||
                      !patientPrimaryIdentifier ||
                      unallowedSensors.includes(sensorType)
                    }
                  />
                  <Typography variant='h6' sx={{ alignSelf: 'center' }}>
                    {sensorType}
                  </Typography>
                </Box>
              );
            })}
          </Box>
          <StyledEmulationActionButton onClick={handleSave} disabled={!isSaveEnabled}>
            Save
          </StyledEmulationActionButton>
        </Box>
      )}
    </EmulatorModalContainer>
  );
};

export default CreatePMModal;
