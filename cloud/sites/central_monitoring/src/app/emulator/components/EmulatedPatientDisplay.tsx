import { EmulatorPatient } from '@/types/emulator';
import {
  StyledEmulationSectionSubtitle,
  StyledEmulationSectionTitle,
} from './EmulatedStyledComponents';
import Box from '@mui/material/Box';
import { styled } from '@mui/material';

interface EmulatedPatientDisplayProps {
  patient?: EmulatorPatient;
}

const EmulatedPatientInfoFieldContainer = styled(Box)(() => ({
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'baseline',
  gap: '15px',
}));

const EmulatedPatientDisplay = ({ patient }: EmulatedPatientDisplayProps) => {
  if (!patient)
    return <StyledEmulationSectionTitle>NO ASSOCIATED PATIENT</StyledEmulationSectionTitle>;
  return (
    <Box>
      <Box sx={{ display: 'flex', flexDirection: 'row', gap: '20px' }}>
        <EmulatedPatientInfoFieldContainer>
          <StyledEmulationSectionTitle>Patient Primary Identifier</StyledEmulationSectionTitle>
          <StyledEmulationSectionSubtitle>{`${patient.primaryIdentifier}`}</StyledEmulationSectionSubtitle>
        </EmulatedPatientInfoFieldContainer>
        <EmulatedPatientInfoFieldContainer>
          <StyledEmulationSectionTitle>Patient Name</StyledEmulationSectionTitle>
          <StyledEmulationSectionSubtitle>{`${patient.givenName} ${patient.familyName}`}</StyledEmulationSectionSubtitle>
        </EmulatedPatientInfoFieldContainer>
      </Box>
      <Box sx={{ display: 'flex', flexDirection: 'row', gap: '20px' }}>
        <EmulatedPatientInfoFieldContainer>
          <StyledEmulationSectionTitle>Patient Gender</StyledEmulationSectionTitle>
          <StyledEmulationSectionSubtitle>{`${patient.gender}`}</StyledEmulationSectionSubtitle>
        </EmulatedPatientInfoFieldContainer>
        <EmulatedPatientInfoFieldContainer>
          <StyledEmulationSectionTitle>Patient Birthdate</StyledEmulationSectionTitle>
          <StyledEmulationSectionSubtitle>{`${patient.birthDate}`}</StyledEmulationSectionSubtitle>
        </EmulatedPatientInfoFieldContainer>
      </Box>
    </Box>
  );
};

export default EmulatedPatientDisplay;
