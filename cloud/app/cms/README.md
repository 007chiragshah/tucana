# Tucana Central Monitoring Station (Electron App)

## Overview

The Central Monitoring Station electron application serves as a desktop container of our Central Monitoring Station web application. It facilitates usage from a desktop computer as a kiosk mode application by opening the web application.

As a shell for the web application, the logic on this component should be kept as simple as possible, leaving the bulk of processing and system interaction to the web application. The responsibilities to be hanled by this electron app are: Managing the Kiosk mode and Configuring the URL to be accessed for the web application

## NPM Scripts

### Most Useful Scripts (Commonly Used)

`npm i`
Installs all dependencies for the project

`npm run start`
Runs the app locally using electron-forge.
Opens the app automatically

`npm run format`
Formats all code files in the project using Prettier.

`npm run check-format`
Checks whether all code files in the project are formatted correctly using Prettier.

`npm run build`
Builds a new application and generates a new installer file using electron-builder
Note: This is the builder we use to generate the installer through our github pipeline

### Other Scripts (Not Used Regularly)

`npm run lint`
Checks whether all code files in the project are formatted correctly using eslint.

`npm run fix-lint`
Formats all code files in the project using eslint.

`npm run package`
Packages the app using electron-forge

`npm run make`
Makes the application using electron-forge

## Flows

### APP START

+_Correct configuration found flow_ immediately opens a chromium full-screen kiosk mode window with the configured URL on the main screen. This flow also detects all other connected display monitors to the computer and opens a stand-by screen on all other displays

+_No configuration / Incorrect configuration flow_ opens a modal which prompts the user for a CMS URL. After the user enters one, it is stored on the `config.ini` file. After this, the correct configuration found flow starts automatically

### AUTHENTICATED

+_Authenticated user detected flow_ is triggered when the main screens title changes to `CMS - Home`. When this happens, all extra screens are opened to the CMS URL home page. It also sends the navigation param for increasing groups for each screen, so in case more groups are available in CMS, they will be displayed on each screen

### FORCE QUIT

+_Force quit flow_ is available for force quitting the app since it's running on kiosk mode. The application can be closed by pressing `Ctrl + Shift + F + Q`.

## STRUCTURE

Since this application is intended to be very small, all code to be run is found inside the `index.js` file in the root of the folder. Other important files and folders are:

`installer.nsh`
NSIS code that handles the custom logic for installation and uninstall for the app when going through the installer run with our build scripts

`/configs`
Configs for the different supported environments

`/images`
Contains the icons to be used by the desktop electron application

## Installation

### Windows

Windows is currently the only officialy supported OS for this application. Running the installer takes the user through a wizard installer. This is controlled by our `installer.nsh` file on the root of this project.

User will be prompted to enter the CMS URL during the installation process. A file called `config.ini` will be created on the current User `%PROGRAMFILES64%` folder containing this information.

## Uninstallation

### Windows

Uninstall should be done through the generated uninstaller file generated during installation. The only extra step the installation does apart from the regular uninstallation process is removing the generated `config.ini` file that was generated either during installation or through regular app usage.
Uninstall will also remove any of the modified registries that the app modified for kiosk mode (if any)

## Set Up Kiosk Mode (Windows 11)

WARNING: THIS MAY MISCONFIGURE YOUR COMPUTER IF MISUSED. READ CAREFULLY BEFORE PROCEEDING.

It is recommended that you set up a Windows Recovery Point before proceeding. It is also recommended that you create a new Administrator Windows User to install this application, instead of using your default administrator user.

When running the app for the first time, Electron will automatically update the Shell Registry inside the Current User WinLogon value. This will ensure the app is run automatically when entering into the account. Electron will also restart the computer automatically so Kiosk mode is fully running from app start.

## Recover From Kiosk Mode

To remove Kiosk Mode, the user can press ctrl+shift+f+q to enable a force quit. This will allow the app to reset the modified registries back to default (disabling kiosk mode) and restart the computer, so full desktop functionality is returned to the user.

### Emergency recovery

After the user has been set in Kiosk Mode through the registry edits, it may be difficult to restore the account for regular usage. If you created a recovery point as recommended, you should follow the following steps to recover:

1. Shut down the computer and enter Recovery Mode (detailed instructions below)
2. Go to See Advanced Repair Options -> Troubleshoot → Advanced options → System Restore
3. Follow the wizard and make sure to select the recovery point that was created before the registry update

In case you don't have a recovery point to recover to, To restore the user to use explorer.exe do the following:

1. Shut down the computer and enter Recovery Mode (detailed instructions below)
2. Go to See Advanced Repair Options -> Troubleshoot → Advanced options → Startup Settings -> Restart
3. Once it restarts, select "Enable Safe Mode with Command Prompt" (usually option 6)
4. Once the command prompt is open, type in the following command:
   ´reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d explorer.exe /f´
5. Restart the computer

### Enter Recovery Mode

1. Press and hold the Shut Down button of the computer for 10 seconds
2. Turn it on again
3. If Windows Logo shows up, repeat steps 1 and 2 (Need to be done between 1 and 4 times usually)
