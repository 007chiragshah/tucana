import AlertOffIcon from '@/components/icons/AlertOffIcon';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { useTheme } from '@mui/material/styles';

type AlertOffProps = {
  height?: number;
  direction?: 'row' | 'column';
};

const AlertOff = ({ height, direction = 'column' }: AlertOffProps) => {
  const theme = useTheme();

  return (
    <Box display='flex' flexDirection={direction} height={height} alignItems='center'>
      {direction == 'column' && <AlertOffIcon />}
      <Typography variant='h6' color={theme.palette.primary.main} lineHeight='16px'>
        Off
      </Typography>
      {direction == 'row' && <AlertOffIcon />}
    </Box>
  );
};

export default AlertOff;
