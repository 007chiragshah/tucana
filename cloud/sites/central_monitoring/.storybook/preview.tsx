import CssBaseline from '@mui/material/CssBaseline';
import { ThemeProvider } from '@mui/material/styles';
import type { Preview } from '@storybook/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { initialize, mswLoader } from 'msw-storybook-addon';
import React from 'react';
import AudioManagerContext from '../src/context/AudioManagerContext';
import PatientsContext from '../src/context/PatientsContext';
import RuntimeConfigProvider from '../src/context/RuntimeContext';
import SessionContext from '../src/context/SessionContext';
import MetricsContext from '../src/context/MetricsContext';
import theme from '../src/theme/theme';
import { setupMoment } from '../src/utils/moment';
import { runtimeConfigStorageName } from '../src/utils/runtime';
import { STORAGE_KEYS } from '../src/utils/storage';
import { I18nextProvider } from 'react-i18next';
import i18n from '../src/app/i18n';

setupMoment();
initialize({
  onUnhandledRequest: 'bypass',
});

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 0,
      staleTime: 0,
      refetchOnWindowFocus: false,
    },
  },
});

const preview: Preview = {
  decorators: [
    (Story) => {
      return (
        <ThemeProvider theme={theme}>
          <QueryClientProvider client={queryClient}>
            <SessionContext>
              <RuntimeConfigProvider>
                <AudioManagerContext>
                  <PatientsContext>
                    <MetricsContext>
                      <I18nextProvider i18n={i18n}>
                        <Story />
                        <CssBaseline />
                      </I18nextProvider>
                    </MetricsContext>
                  </PatientsContext>
                </AudioManagerContext>
              </RuntimeConfigProvider>
            </SessionContext>
          </QueryClientProvider>
        </ThemeProvider>
      );
    },
    (Story) => {
      const config = {
        APP_URL: '',
      };

      window.localStorage.setItem(runtimeConfigStorageName, JSON.stringify(config));
      localStorage.setItem(STORAGE_KEYS.ACCESS_TOKEN, 'accessToken');
      return <Story />;
    },
  ],
  parameters: {
    layout: 'centered',
    actions: { argTypesRegex: '^on[A-Z].*' },
    nextjs: {
      appDirectory: true,
    },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
  },
  loaders: [mswLoader],
};

export default preview;
