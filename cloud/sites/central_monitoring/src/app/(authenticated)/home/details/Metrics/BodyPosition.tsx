import Loading from '@/app/loading';
import BodyAngleIcon from '@/components/icons/BodyAngleIcon';
import AlertOffIcon from '@/components/icons/AlertOffIcon';
import LeftLBodyPositionIcon from '@/components/icons/bodyPositions/LeftLBodyPositionIcon';
import ProneBodyPositionIcon from '@/components/icons/bodyPositions/ProneBodyPositionIcon';
import RightLBodyPositionIcon from '@/components/icons/bodyPositions/RightLBodyPositionIcon';
import SupineBodyPositionIcon from '@/components/icons/bodyPositions/SupineBodyPositionIcon';
import UprightBodyPositionIcon from '@/components/icons/bodyPositions/UprightBodyPositionIcon';
import { ERROR_VALUE, disabledColor } from '@/constants';
import { getAlertClass } from '@/utils/alertUtils';
import { openSansFont } from '@/utils/fonts';
import { ALERT_PRIORITY, POSITION_TYPES } from '@/utils/metricCodes';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { alpha, styled, useTheme } from '@mui/material/styles';
import AlertOff from '@/app/(authenticated)/home/details/Metrics/AlertOff';

const BodyPositionAlertStatus = ({ alertConditionEnabled }: { alertConditionEnabled: boolean }) =>
  alertConditionEnabled ? <Box height={42} /> : <AlertOff height={42} />;
const TimeContainer = styled(Grid, {
  shouldForwardProp: (prop) => prop !== 'color',
})<{ color?: string }>(({ color }) => ({
  display: 'flex',
  alignItems: 'baseline',
  color: color,
  gap: 2,
  height: 34,
}));
const TimeUnit = styled(Typography)(() => ({
  fontSize: 14,
  fontWeight: 600,
  lineHeight: 'normal',
  fontFamily: openSansFont.style.fontFamily,
}));
const Label = styled(Typography)(() => ({
  fontSize: 17,
  fontWeight: 600,
  lineHeight: '23px',
  fontFamily: openSansFont.style.fontFamily,
}));
const RightContainer = styled(Grid)(() => ({
  flexDirection: 'column',
  alignContent: 'flex-end',
  justifyContent: 'flex-end',
}));
const Container = styled(Grid)(({ theme }) => ({
  display: 'flex',
  flexDirection: 'row',
  justifyContent: 'space-between',
  padding: theme.spacing(6, 8),
}));

interface BodyPositionIconProps {
  position: POSITION_TYPES;
  darkIcon: boolean;
}

const BodyPositionIcon = ({ position, darkIcon }: BodyPositionIconProps) => {
  switch (position) {
    case POSITION_TYPES.SUPINE:
      return <SupineBodyPositionIcon darkIcon={darkIcon} />;
    case POSITION_TYPES.PRONE:
      return <ProneBodyPositionIcon darkIcon={darkIcon} />;
    case POSITION_TYPES.UPRIGHT:
      return <UprightBodyPositionIcon darkIcon={darkIcon} />;
    case POSITION_TYPES.RIGHTL:
      return <RightLBodyPositionIcon darkIcon={darkIcon} />;
    case POSITION_TYPES.LEFTL:
      return <LeftLBodyPositionIcon darkIcon={darkIcon} />;
    default:
      return null;
  }
};

const getBodyPositionText = (position: POSITION_TYPES) => {
  switch (position) {
    case POSITION_TYPES.SUPINE:
      return 'Supine';
    case POSITION_TYPES.PRONE:
      return 'Prone';
    case POSITION_TYPES.UPRIGHT:
      return 'Upright';
    case POSITION_TYPES.RIGHTL:
      return 'Right-L';
    case POSITION_TYPES.LEFTL:
      return 'Left-L';
    default:
      return 'Body position';
  }
};

interface BodyAngleProps {
  angle?: number | string | null;
  isError?: boolean;
  color?: string;
  alertPriority?: ALERT_PRIORITY;
}

const BodyAngle = ({ angle = null, isError = false, alertPriority, color }: BodyAngleProps) => {
  const theme = useTheme();

  return (
    <Box
      alignSelf='end'
      display='flex'
      flexDirection='row'
      justifyContent='center'
      alignItems='flex-end'
    >
      <BodyAngleIcon darkIcon={!!alertPriority} color={color} />
      <Label
        sx={{
          color: color || (alertPriority ? theme.palette.common.black : theme.palette.divider),
        }}
      >
        {isError ? ERROR_VALUE : angle || angle === 0 ? `${angle}°` : '-'}
      </Label>
    </Box>
  );
};

interface BodyPositionProps {
  position?: POSITION_TYPES | null;
  angle?: number | string | null;
  alertPriority?: ALERT_PRIORITY;
  hoursInCurrentPosition: string;
  minutesInCurrentPosition: string;
  isLoading: boolean;
  isConnected: boolean;
  hasTechnicalAlert: boolean;
  alertConditionEnabled: boolean;
}

const BodyPosition = ({
  position = null,
  angle = null,
  alertPriority,
  isConnected,
  hoursInCurrentPosition,
  minutesInCurrentPosition,
  isLoading,
  hasTechnicalAlert,
  alertConditionEnabled,
}: BodyPositionProps) => {
  const theme = useTheme();
  const containerStyle = {
    height: 100,
    paddingTop: 2,
    paddingLeft: 8,
    paddingRight: 8,
    paddingBottom: 5,
  };
  const loadingContainerStyle = {
    height: 100,
    paddingTop: 6,
    paddingLeft: 8,
    paddingRight: 8,
    paddingBottom: 5,
  };

  if (!isConnected) {
    return (
      <Container
        data-testid='position-metric-card position-sensors-not-connected'
        className='metricCard'
        style={containerStyle}
      >
        <Grid
          display='flex'
          flexDirection='column'
          justifyContent='space-between'
          alignItems='flex-start'
        >
          <Label
            sx={{
              color: disabledColor,
              maxWidth: '40%',
            }}
          >
            Body Position
          </Label>
          <BodyPositionAlertStatus alertConditionEnabled={alertConditionEnabled} />
        </Grid>
        <RightContainer container>
          <BodyAngle color={alpha(theme.palette.divider, 0.35)} />
          <Grid style={{ height: 54 }} container flexDirection='column' alignItems='flex-end'>
            <Label
              sx={{
                display: 'flex',
                alignItems: 'center',
                textAlign: 'right',
                color: disabledColor,
                marginBottom: -4,
                height: 24,
              }}
            >
              Lasted
            </Label>
            <TimeContainer color={disabledColor}>
              <Typography variant='metricNumberStyles'>00</Typography>
              <TimeUnit>h</TimeUnit>
              <Typography variant='metricNumberStyles'>00</Typography>
              <TimeUnit>m</TimeUnit>
            </TimeContainer>
          </Grid>
        </RightContainer>
      </Container>
    );
  }

  if (isLoading) {
    return (
      <Container className='metricCard' style={loadingContainerStyle}>
        <Grid
          display='flex'
          flexDirection='column'
          justifyContent='space-between'
          alignItems='flex-start'
        >
          <Label
            sx={{
              color: 'divider',
              maxWidth: '40%',
            }}
          >
            Body Position
          </Label>
          <BodyPositionAlertStatus alertConditionEnabled={alertConditionEnabled} />
        </Grid>
        <RightContainer
          container
          style={{
            justifyContent: 'space-between',
          }}
        >
          <BodyAngle />
          <Grid style={{ height: 54 }} container flexDirection='column' alignItems='flex-end'>
            <Label>&nbsp;</Label>
            <Loading height={32} thickness={2.5} size={40} />
          </Grid>
        </RightContainer>
      </Container>
    );
  }

  return (
    <Container
      data-testid='position-metric-card position-sensors-connected'
      className={`
          metricCard 
          ${getAlertClass(alertPriority)}
          `}
      style={containerStyle}
    >
      {!hasTechnicalAlert && position ? (
        <Grid
          display='flex'
          flexDirection='column'
          justifyContent='space-between'
          alignItems='flex-start'
        >
          <BodyPositionIcon position={position} darkIcon={!!alertPriority} />
          <Label
            sx={{
              color: alertPriority ? theme.palette.common.black : theme.palette.divider,
            }}
          >
            {getBodyPositionText(position)}
          </Label>
          <BodyPositionAlertStatus alertConditionEnabled={alertConditionEnabled} />
        </Grid>
      ) : (
        <Grid
          display='flex'
          flexDirection='column'
          justifyContent='space-between'
          alignItems='flex-start'
        >
          <Label
            sx={{
              color: alertPriority ? theme.palette.common.black : theme.palette.divider,
              maxWidth: '40%',
            }}
          >
            Body Position
          </Label>
          <BodyPositionAlertStatus alertConditionEnabled={alertConditionEnabled} />
        </Grid>
      )}
      <RightContainer container>
        <BodyAngle
          angle={angle}
          isError={hasTechnicalAlert || !position}
          alertPriority={alertPriority}
        />
        <Grid style={{ height: 54 }} container flexDirection='column' alignItems='flex-end'>
          <Label
            sx={{
              display: 'flex',
              alignItems: 'center',
              textAlign: 'right',
              color: alertPriority ? theme.palette.common.black : theme.palette.divider,
              marginBottom: -4,
              height: 24,
            }}
          >
            Lasted
          </Label>
          {hasTechnicalAlert || !position ? (
            <TimeContainer
              className={openSansFont.className}
              color={alertPriority ? theme.palette.common.black : theme.palette.divider}
            >
              <Typography variant='metricNumberStyles'>{ERROR_VALUE}</Typography>
            </TimeContainer>
          ) : (
            <TimeContainer
              color={alertPriority ? theme.palette.common.black : theme.palette.divider}
            >
              <Typography variant='metricNumberStyles'>{hoursInCurrentPosition}</Typography>
              <TimeUnit>h</TimeUnit>
              <Typography variant='metricNumberStyles'>{minutesInCurrentPosition}</Typography>
              <TimeUnit>m</TimeUnit>
            </TimeContainer>
          )}
        </Grid>
      </RightContainer>
    </Container>
  );
};

export default BodyPosition;
