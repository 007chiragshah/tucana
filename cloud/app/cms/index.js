const { app, session, BrowserWindow, ipcMain, screen, globalShortcut } = require('electron');
const path = require('path');
const fs = require('fs');
const { exec, execSync } = require('child_process');
const windowOptions = {
  fullscreen: true,
  frame: false,
  kiosk: true,
};

let loginWindow;
let dialogWindow;
let manualClose = false;

const programFilesPath = process.env.ProgramFiles;
const configPath = path.join(programFilesPath, 'CentralHub', 'config.ini');

const getShellValueExists = () => {
  try {
    const result = execSync(
      'reg query "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Shell',
      { encoding: 'utf-8' }
    );
    if (result) {
      return true;
    }
  } catch (error) {
    console.error('Error reading registry:', error);
  }
  return false;
};

const addShellRegistryValue = () => {
  exec(
    'reg add "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Shell /t REG_SZ /d "C:\\Program Files\\CMSKiosk\\CMSKiosk.exe" /f',
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing command: ${error.message}`);
        return;
      }
      if (stderr) {
        console.error(`stderr: ${stderr}`);
        return;
      }
    }
  );
};

const removeShellRegistryValue = () => {
  exec(
    'reg delete "HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Shell /f',
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error deleting Shell value: ${error}`);
        return;
      }
    }
  );
};

const openExplorerAndQuit = () => {
  removeShellRegistryValue();

  // Wait for registry change to apply, then restart the computer
  setTimeout(() => {
    exec('shutdown /r /f /t 0', (error, stdout, stderr) => {
      if (error) {
        console.error(`Error restarting computer: ${error}`);
        return;
      }
    });
  }, 1500);
};

const parseIni = (content) => {
  const result = {};
  const lines = content.split(/\r?\n/);
  for (const line of lines) {
    if (line.trim() === '' || line.startsWith('[')) continue; // Skip empty lines and section headers
    const [key, value] = line.split('=');
    result[key.trim()] = value.trim();
  }
  return result;
};

const createWindows = () => {
  const windows = [];
  // PRIMARY DISPLAY SETUP
  const primaryDisplay = screen.getPrimaryDisplay();
  const { width, height } = primaryDisplay.workAreaSize;
  loginWindow = new BrowserWindow({
    ...windowOptions,
    width,
    height,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      partition: 'persist:cms',
    },
  });
  const dir = path.dirname(configPath);
  if (!fs.existsSync(dir) || !fs.existsSync(configPath)) {
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(configPath, '', (err) => {
      if (err) console.error('Error creating .ini file:', err);
    });
  }
  fs.readFile(configPath, 'utf8', (err, data) => {
    let config;
    if (err) {
      console.error('Error reading config file:', err);
    } else {
      config = parseIni(data);
    }

    if (config && config.CMS_URL && config.CMS_URL !== undefined && config.CMS_URL !== '') {
      // Load URL in primary screen
      loginWindow.loadURL(config.CMS_URL);
    } else {
      // Load index.html by default
      loginWindow.loadFile(path.join(__dirname, 'renderer', 'index.html'));
      createEnvironmentDialog();
    }
  });

  loginWindow.on('close', (event) => {
    if (!manualClose) {
      event.preventDefault();
    }
  });

  // EXTERNAL DISPLAYS SETUP
  const displays = screen.getAllDisplays();
  const externalDisplay = displays.filter((display) => {
    return display.bounds.x !== 0 || display.bounds.y !== 0;
  });
  if (externalDisplay) {
    externalDisplay.forEach((display) => {
      const window = new BrowserWindow({
        ...windowOptions,
        x: display.bounds.x + 50,
        y: display.bounds.y + 50,
        webPreferences: {
          partition: 'persist:cms',
        },
      });
      window.loadFile(path.join(__dirname, 'renderer', 'index.html'));
      windows.push(window);
      // TODO: prevent default close
      window.on('close', (event) => {
        event.preventDefault();
      });
    });
    loginWindow.on('page-title-updated', (_, title) => {
      // loadURL if title changes to login
      if (title === 'CMS - Home') {
        windows.forEach((display, index) => {
          display.webContents.session = loginWindow.webContents.session.getUserAgent();
          display.loadURL(
            loginWindow.webContents.getURL() + '?groupIndex=' + (index + 1) + '&hideSetup=1'
          );
        });
      } else {
        windows.forEach((display, _) => {
          display.loadFile(path.join(__dirname, 'renderer', 'index.html'));
        });
      }
    });
  }
};

const handleModeSelected = (selectedMode) => {
  if (selectedMode === 'disabled') {
    createWindows();
  } else {
    const shellValueExists = getShellValueExists();

    if (!shellValueExists) {
      addShellRegistryValue();
      exec('shutdown /r /f /t 0', (error, stdout, stderr) => {
        if (error) {
          console.error(`Error restarting computer: ${error}`);
          return;
        }
      });
    } else {
      createWindows();
    }
  }
};

const createModeSelectionDialog = () => {
  const windows = [];
  const primaryDisplay = screen.getPrimaryDisplay();
  const { width, height } = primaryDisplay.workAreaSize;
  const modeSelectionWindow = new BrowserWindow({
    ...windowOptions,
    width,
    height,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });
  modeSelectionWindow.loadFile(path.join(__dirname, 'renderer', 'modeSelection.html'));

  //External Displays
  const displays = screen.getAllDisplays();
  const externalDisplay = displays.filter((display) => {
    return display.bounds.x !== 0 || display.bounds.y !== 0;
  });
  if (externalDisplay) {
    externalDisplay.forEach((display) => {
      const window = new BrowserWindow({
        ...windowOptions,
        x: display.bounds.x + 50,
        y: display.bounds.y + 50,
      });
      window.loadFile(path.join(__dirname, 'renderer', 'index.html'));
      windows.push(window);
    });
  }

  ipcMain.on('kiosk-selection', (_, modeSelected) => {
    modeSelectionWindow.close();
    windows.forEach((display) => {
      display.close();
    });
    handleModeSelected(modeSelected);
  });
};

const createEnvironmentDialog = async () => {
  dialogWindow = new BrowserWindow({
    icon: path.join(__dirname, 'images/desktop-icon.png'),
    modal: true,
    parent: loginWindow,
    width: 500,
    height: 300,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });
  dialogWindow.on('close', (event) => {
    event.preventDefault();
  });
  dialogWindow.loadFile(path.join(__dirname, 'renderer', 'envPrompt.html'));
  ipcMain.on('mode-selected', (_, appUrl) => {
    const dir = path.dirname(configPath);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    fs.writeFile(configPath, `CMS_URL=${appUrl}`, (err) => {
      if (err) console.error('Error writing to .ini file:', err);
    });
    loginWindow.loadURL(appUrl + '?groupIndex=0');
    dialogWindow.close();
  });
  dialogWindow.on('closed', () => {
    dialogWindow = null;
  });
};
app.on('ready', () => {
  const sharedSession = session.fromPartition('persist:cms');
  session.defaultSession = sharedSession;
});

app.on('will-quit', () => {
  globalShortcut.unregisterAll();
});

app.commandLine.appendSwitch('disable-features', 'HardwareMediaKeyHandling,MediaSessionService');
app.whenReady().then(() => {
  globalShortcut.register('Shift+Ctrl+F+Q', () => {
    manualClose = true;
    openExplorerAndQuit();
  });

  createModeSelectionDialog();
});
