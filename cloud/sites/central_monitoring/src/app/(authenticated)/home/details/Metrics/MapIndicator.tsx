import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { styled, Theme } from '@mui/material/styles';
import { get } from 'lodash';
import Loading from '@/app/loading';
import { ERROR_VALUE } from '@/constants';

type MapIndicatorProps = {
  measurement: number | string | undefined;
  isLoading: boolean;
  hasAlert: boolean;
  hasTechnicalAlert?: boolean;
  hasError: boolean;
};

const MapText = styled(Typography, {
  shouldForwardProp: (prop) => prop !== 'color',
})<{ color?: string }>(({ color }) => ({
  lineHeight: '34px',
  color: color,
}));

const MapIndicator = ({
  hasAlert,
  hasTechnicalAlert = false,
  measurement,
  hasError,
  isLoading,
}: MapIndicatorProps) => {
  return (
    <Grid
      display='flex'
      flexDirection='row'
      alignSelf='flex-end'
      justifyContent='space-between'
      marginRight={23}
    >
      <MapText
        sx={{
          color: (theme: Theme) =>
            hasTechnicalAlert
              ? get(theme.palette, 'alert.low')
              : hasAlert
              ? theme.palette.common.black
              : theme.palette.divider,
        }}
      >
        MAP
      </MapText>
      <Typography
        variant='metricNumberStyles'
        sx={{
          justifyContent: 'center',
          margin: (theme: Theme) => theme.spacing(0, 8),
          lineHeight: '34px',
          color: (theme: Theme) =>
            hasTechnicalAlert
              ? get(theme.palette, 'alert.low')
              : hasAlert
              ? theme.palette.common.black
              : theme.palette.divider,
        }}
      >
        {'('}
      </Typography>
      <Grid minWidth={32}>
        {isLoading ? (
          <Grid display='flex' justifyContent='flex-end'>
            <Loading height='100%' size={32} thickness={2.5} />
          </Grid>
        ) : (
          <Typography
            data-testid={`metric-value-nibp-map-${String(
              hasError || hasTechnicalAlert ? ERROR_VALUE : measurement
            )}`}
            variant='metricNumberStyles'
            sx={{
              color: (theme: Theme) =>
                hasTechnicalAlert
                  ? get(theme.palette, 'alert.low')
                  : hasAlert
                  ? theme.palette.common.black
                  : theme.palette.divider,
              whiteSpace: 'nowrap',
              lineHeight: '34px',
            }}
          >
            {hasError || hasTechnicalAlert ? ERROR_VALUE : measurement}
          </Typography>
        )}
      </Grid>
      <Typography
        variant='metricNumberStyles'
        sx={{
          justifyContent: 'center',
          margin: (theme: Theme) => theme.spacing(0, 8),
          lineHeight: '34px',
          color: (theme: Theme) =>
            hasTechnicalAlert
              ? get(theme.palette, 'alert.low')
              : hasAlert
              ? theme.palette.common.black
              : theme.palette.divider,
        }}
      >
        {')'}
      </Typography>
    </Grid>
  );
};

export default MapIndicator;
