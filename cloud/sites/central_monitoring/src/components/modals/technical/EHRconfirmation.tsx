import Button from '@mui/material/Button';
import DialogContent from '@mui/material/DialogContent';
import Modal from '@mui/material/Modal';
import { useRef } from 'react';
import ConfirmationModalContainer from '../container/ConfirmationModalContainer';
import Grid from '@mui/material/Grid';
import { Label, Value } from '@/styles/StyledComponents';
import { useTranslation } from 'react-i18next';

interface EHRconfirmationModalProps {
  isOpen: boolean;
  host: string;
  port: number;
  interval: number;
  onBackToEdit: () => void;
  onConfirm: () => void;
}

const EHRconfirmationModal = ({
  isOpen,
  onBackToEdit,
  onConfirm,
  host,
  port,
  interval,
}: EHRconfirmationModalProps) => {
  const modalRef = useRef<HTMLDivElement>(null);
  const { t } = useTranslation();

  return (
    <Modal open={isOpen} sx={{ display: 'flex', flex: 1 }}>
      <DialogContent sx={{ margin: 'auto', outline: 'none' }}>
        <ConfirmationModalContainer
          ref={modalRef}
          title={t('TechnicalHome.confirmationTitle')}
          description={''}
        >
          <Grid container flex={1} flexDirection='column' gap={1} overflow='auto'>
            <Grid display='flex' flexDirection='row' gap={24} paddingY={16}>
              <Label variant='body2'>{t('TechnicalHome.hostAddressTitle')}</Label>
              <Value variant='body1'>{host}</Value>
            </Grid>
            <Grid display='flex' flexDirection='row' gap={24} paddingY={16}>
              <Label variant='body2'>{t('TechnicalHome.serverPortTitle')}</Label>
              <Value variant='body1'>{port}</Value>
            </Grid>
            <Grid display='flex' flexDirection='row' gap={24} paddingY={16}>
              <Label variant='body2'>{t('TechnicalHome.transmisionIntervalTitle')}</Label>
              <Value variant='body1'>{interval}</Value>
            </Grid>
          </Grid>
          <Button
            variant='contained'
            fullWidth
            onClick={onConfirm}
            sx={{ my: 24 }}
            data-testid='confirm-button'
          >
            {t('GenericButtons.confirmButton')}
          </Button>
          <Button
            variant='outlined'
            fullWidth
            onClick={onBackToEdit}
            data-testid='back-to-edit-button'
          >
            {t('GenericButtons.backToEditButton')}
          </Button>
        </ConfirmationModalContainer>
      </DialogContent>
    </Modal>
  );
};

export default EHRconfirmationModal;
