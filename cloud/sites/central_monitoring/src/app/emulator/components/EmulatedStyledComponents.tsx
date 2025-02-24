import { openSansFont } from '@/utils/fonts';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';
import { styled } from '@mui/material/styles';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';

export const StyledEmulationSectionTitle = styled(Typography)(() => ({
  fontSize: '22px',
  marginTop: '15px',
  fontWeight: '600',
  textDecoration: 'underline',
}));

export const StyledEmulationSectionSubtitle = styled(Typography)(() => ({
  marginTop: '5px',
}));

export const StyledEmulationMenuItem = styled(MenuItem)(() => ({
  color: '#EFF0F1',
  fontFamily: openSansFont.style.fontFamily,
  fontSize: 18,
  fontWeight: 400,
  lineHeight: '27px',
}));

export const StyledEmulationActionButton = styled(Button)(() => ({
  border: '1px solid white',
  borderRadius: '16px',
  width: '25%',
  alignSelf: 'center',
}));

export const StyledEmulationTextField = styled(TextField)(() => ({
  '&.MuiTextField-root .MuiOutlinedInput-notchedOutline': {
    border: 'none',
  },
  '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
    border: 'none',
  },
  '&.Mui-error .MuiOutlinedInput-notchedOutline': {
    border: 'none',
  },
}));

export const StyledEmulatedPMContainer = styled(Box)(() => ({
  overflowX: 'scroll',
}));
