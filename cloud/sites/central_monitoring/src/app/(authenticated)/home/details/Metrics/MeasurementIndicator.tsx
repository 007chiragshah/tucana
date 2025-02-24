import Loading from '@/app/loading';
import { DISPLAY_DIRECTION, ERROR_VALUE, disabledColor } from '@/constants';
import { ThresholdText } from '@/styles/StyledComponents';
import { Measurement } from '@/types/metrics';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { Theme, useTheme } from '@mui/material/styles';
import { get } from 'lodash';
import { useEffect, useState } from 'react';
import AlertOff from '@/app/(authenticated)/home/details/Metrics/AlertOff';

type MeasurementProps = {
  measurement: Measurement;
  hasAlert: boolean;
  hasTechnicalAlert: boolean;
  isLoading: boolean;
  isError: boolean;
  isConnected: boolean;
  testid: string;
  showDisconnectedData: boolean;
  direction?: DISPLAY_DIRECTION;
  disableMeasurementLimits?: boolean;
};

const MeasurementReading = ({
  measurement,
  hasAlert,
  hasTechnicalAlert,
  isLoading,
  isError,
  isConnected,
  testid,
  showDisconnectedData,
  direction = DISPLAY_DIRECTION.LTR,
  disableMeasurementLimits = false,
}: MeasurementProps) => {
  const theme = useTheme();
  const [displayedValue, setDisplayedValue] = useState<string | number>('');

  useEffect(() => {
    if (isError) setDisplayedValue(ERROR_VALUE);
  }, [isError]);

  useEffect(() => {
    if (!isError && measurement.value) setDisplayedValue(measurement.value);
  }, [isError, measurement]);

  const textColor =
    !isConnected && !showDisconnectedData
      ? disabledColor
      : hasTechnicalAlert
      ? get(theme.palette, 'alert.low')
      : hasAlert
      ? theme.palette.common.black
      : theme.palette.divider;

  return (
    <Grid
      display='flex'
      flex={1}
      width='100%'
      height='43px'
      flexDirection={direction === DISPLAY_DIRECTION.LTR ? 'row' : 'row-reverse'}
      alignSelf='center'
      justifyContent='space-between'
    >
      <Grid
        sx={{
          lineHeight: '15px',
          margin: (theme: Theme) =>
            direction === DISPLAY_DIRECTION.LTR
              ? `${theme.spacing(0, 9, 0, 0)}`
              : `${theme.spacing(0, 0, 0, 9)}`,
          whiteSpace: 'nowrap',
        }}
        alignSelf='center'
      >
        {!disableMeasurementLimits &&
          (!measurement.upperLimit && !measurement.lowerLimit ? (
            <AlertOff />
          ) : (
            <>
              {measurement.upperLimit ? (
                <ThresholdText color={textColor}>{measurement.upperLimit}</ThresholdText>
              ) : (
                <AlertOff direction={'row'} />
              )}
              {measurement.lowerLimit ? (
                <ThresholdText color={textColor}>{measurement.lowerLimit}</ThresholdText>
              ) : (
                <AlertOff direction={'row'} />
              )}
            </>
          ))}
      </Grid>

      {isConnected || showDisconnectedData ? (
        !displayedValue &&
        !showDisconnectedData &&
        (isLoading || measurement.value == undefined) ? (
          <Grid display='flex' justifyContent='flex-end'>
            <Loading height='100%' size={32} thickness={2.5} />
          </Grid>
        ) : (
          <Typography
            data-testid={`metric-value-${testid}`}
            variant='metricNumberStyles'
            sx={{
              color: textColor,
              whiteSpace: 'nowrap',
            }}
          >
            {displayedValue}
          </Typography>
        )
      ) : null}
    </Grid>
  );
};

interface MeasurementIndicatorProps {
  hasAlert?: boolean;
  hasTechnicalAlert?: boolean;
  isLoading?: boolean;
  isError?: boolean;
  isConnected?: boolean;
  measurement: Measurement;
  testid: string;
  showDisconnectedData?: boolean;
  disableMeasurementLimits?: boolean;
}

const MeasurementIndicator = ({
  hasAlert = false,
  hasTechnicalAlert = false,
  isLoading = false,
  isError = false,
  isConnected = false,
  measurement,
  testid,
  showDisconnectedData = false,
  disableMeasurementLimits = false,
}: MeasurementIndicatorProps) => (
  <Grid
    data-testid={testid}
    display='flex'
    width='100%'
    flexDirection='row'
    alignSelf='center'
    justifyContent='space-between'
  >
    <MeasurementReading
      measurement={measurement}
      hasAlert={hasAlert}
      hasTechnicalAlert={hasTechnicalAlert}
      isLoading={isLoading}
      isError={isError}
      isConnected={isConnected}
      showDisconnectedData={showDisconnectedData}
      testid={testid}
      disableMeasurementLimits={disableMeasurementLimits}
    />
  </Grid>
);

export default MeasurementIndicator;
export { MeasurementReading };
