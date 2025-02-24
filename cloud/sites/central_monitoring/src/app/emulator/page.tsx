'use client';

import Box from '@mui/material/Box';
import CreatePMModal from './CreatePMModal';
import { ReactElement, useMemo, useState } from 'react';
import { PatientGender } from '@/types/patient';
import { SENSOR_TYPES } from '@/types/sensor';
import { useCreateEmulatedPM } from '@/api/useCreateEmulatedPM';
import {
  StyledEmulatedPMContainer,
  StyledEmulationActionButton,
  StyledEmulationSectionTitle,
} from './components/EmulatedStyledComponents';
import { useEmulatorMonitors } from '@/api/useEmulatorMonitors';
import Typography from '@mui/material/Typography';
import PMDataModal from './PMDataModal';
import { useDisconnectEmulatedPM } from '@/api/useDisconnectEmulatedPM';
import Loading from '../loading';
import {
  SendEmulatedAlertRequest,
  useSendEmulatedVitalAlert,
} from '@/api/useSendEmulatedVitalAlert';
import { useSendEmulatedTechnicalAlert } from '@/api/useSendEmulatedTechnicalAlert';

export type PMCreationPayload = {
  pmPrimaryIdentifier: string;
  pmName: string;
  patient?: {
    patientPrimaryIdentifier: string;
    patientGivenName: string;
    patientFamilyName: string;
    patientGender: PatientGender;
    patientBirthDate: string;
  };
  sensors: SENSOR_TYPES[];
};

/**
 * Screen only for internal usage. Not intended for final user. Handles flows
 * with the emulator to simulate different cases. Has no use in production
 * environments since there is no emulator there
 */
const EmulatorController = () => {
  const [showCreatePMModal, setShowCreatePmModal] = useState<boolean>(false);
  const [showPMDataModal, setShowPMDatamodal] = useState<boolean>(false);
  const [selectedPM, setSelectedPM] = useState<string>('');

  const { createEmulatedPM } = useCreateEmulatedPM();
  const { disconnectEmulatedPM } = useDisconnectEmulatedPM();
  const { sendEmulatedVitalAlert } = useSendEmulatedVitalAlert();
  const { sendEmulatedTechnicalAlert } = useSendEmulatedTechnicalAlert();
  const emulatedPMs = useEmulatorMonitors();

  const handlePMCreation = async (payload: PMCreationPayload) => {
    const result = await createEmulatedPM(payload);
    // TODO: HANDLE ERROR?

    if (result.status >= 200 && result.status < 300) {
      void emulatedPMs.refetch();
      setShowCreatePmModal(false);
    }
  };

  const handlePMSelection = (pmPrimaryIdentifier: string) => {
    setSelectedPM(pmPrimaryIdentifier);
    setShowPMDatamodal(true);
  };

  const handlePMDisconnection = async (pmPrimaryIdentifier: string) => {
    const result = await disconnectEmulatedPM(pmPrimaryIdentifier);
    // TODO: HANDLE ERROR?

    if (result.status >= 200 && result.status < 300) {
      void emulatedPMs.refetch();
      setShowPMDatamodal(false);
    }
  };

  const handleSendVitalAlert = async (payload: SendEmulatedAlertRequest) => {
    const result = await sendEmulatedVitalAlert(payload);
    // TODO: HANDLE ERROR?

    if (result.status >= 200 && result.status < 300) {
      setShowPMDatamodal(false);
    }
  };

  const handleSendTechnicalAlert = async (payload: SendEmulatedAlertRequest) => {
    const result = await sendEmulatedTechnicalAlert(payload);
    // TODO: HANDLE ERROR?

    if (result.status >= 200 && result.status < 300) {
      setShowPMDatamodal(false);
    }
  };

  const renderedPMS = useMemo(() => {
    const res: ReactElement[] = [];
    emulatedPMs.data.forEach((singlePM) => {
      res.push(
        <Typography
          id={`pm_title_${singlePM.primaryIdentifier}`}
          key={`pm_title_${singlePM.primaryIdentifier}`}
          onClick={() => {
            handlePMSelection(singlePM.primaryIdentifier);
          }}
          sx={{ cursor: 'pointer', mt: '10px' }}
        >
          {singlePM.primaryIdentifier}
        </Typography>
      );
    });
    return res;
  }, [emulatedPMs.data]);

  return (
    <Box
      sx={{
        justifyContent: 'center',
        display: 'flex',
        flexDirection: 'column',
        width: '95%',
        ml: '2.5%',
        height: '100%',
      }}
    >
      {emulatedPMs.isFetching || emulatedPMs.isLoading ? (
        <Box display='flex' width='100%' height='100%' alignContent='center' flexWrap='wrap'>
          <Loading height={96} size={96} />
        </Box>
      ) : (
        <Box sx={{ width: '100%', height: '100%', display: 'flex', flexDirection: 'column' }}>
          <CreatePMModal
            isOpen={showCreatePMModal}
            onClose={() => {
              setShowCreatePmModal(false);
            }}
            isLoading={emulatedPMs.isFetching || emulatedPMs.isLoading}
            onSave={(payload: PMCreationPayload) => void handlePMCreation(payload)}
          />
          <PMDataModal
            isOpen={showPMDataModal}
            isLoading={emulatedPMs.isFetching || emulatedPMs.isLoading}
            pmData={emulatedPMs?.data.find((singlePM) => singlePM.primaryIdentifier === selectedPM)}
            onClose={() => {
              setShowPMDatamodal(false);
            }}
            onDisconnect={(pmPrimaryIdentifier) => void handlePMDisconnection(pmPrimaryIdentifier)}
            onSendVitalAlert={(payload: SendEmulatedAlertRequest) =>
              void handleSendVitalAlert(payload)
            }
            onSendTechnicalAlert={(payload: SendEmulatedAlertRequest) =>
              void handleSendTechnicalAlert(payload)
            }
          />
          <StyledEmulationActionButton
            sx={{ marginTop: '15px' }}
            onClick={() => {
              setShowCreatePmModal(true);
            }}
          >
            Create New PM
          </StyledEmulationActionButton>
          <StyledEmulationSectionTitle>
            All Current Emulated PMs (click on any for more options)
          </StyledEmulationSectionTitle>
          <StyledEmulatedPMContainer>{renderedPMS}</StyledEmulatedPMContainer>
        </Box>
      )}
    </Box>
  );
};

export default EmulatorController;
