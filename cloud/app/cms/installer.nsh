!include "MUI2.nsh"
!include "LogicLib.nsh"

RequestExecutionLevel admin

Var TextField
Var InputValue
Var CustomWindow
Var LocalAppDir

!macro IsUserAdmin RESULT
 !define Index "Line${__LINE__}"
   StrCpy ${RESULT} 0
   System::Call '*(&i1 0,&i4 0,&i1 5)i.r0'
   System::Call 'advapi32::AllocateAndInitializeSid(i r0,i 2,i 32,i 544,i 0,i 0,i 0,i 0,i 0, \
   i 0,*i .R0)i.r5'
   System::Free $0
   System::Call 'advapi32::CheckTokenMembership(i n,i R0,*i .R1)i.r5'
   StrCmp $5 0 ${Index}_Error
   StrCpy ${RESULT} $R1
   Goto ${Index}_End
 ${Index}_Error:
   StrCpy ${RESULT} -1
 ${Index}_End:
   System::Call 'advapi32::FreeSid(i R0)i.r5'
 !undef Index
!macroend

Function OnTextChange
    ${NSD_GetText} $TextField $InputValue
    StrCmp $InputValue "" 0 +3
    ; Empty string block
    EnableWindow $CustomWindow 0
    Goto +2
    ; Non-Empty string block
    EnableWindow $CustomWindow 1
FunctionEnd

Function urlPageCreate
    !insertmacro IsUserAdmin $0

    ${If} $0 == 1
        !insertmacro MUI_HEADER_TEXT "URL Config" "Configure the URL to be used for the CMS App"

        GetDlgItem $CustomWindow $HWNDPARENT 1
        EnableWindow $CustomWindow 0

        nsDialogs::Create 1018
        Pop $0
        ${If} $0 == error
            Abort
        ${EndIf}

        ${NSD_CreateLabel} 0 0 100% 12u "Enter CMS URL: "

        ${NSD_CreateText} 10u 25u 200u 12u ""
        Pop $TextField
        ${NSD_OnChange} $TextField OnTextChange

        ; Create the new label just below the TextField
        ${NSD_CreateLabel} 0 50u 100% 24u "Note: When pressing the install button below, the installer will check for connection to the entered URL. Screen may take a couple seconds to update after pressing the button."

        nsDialogs::Show
    ${EndIf}

FunctionEnd

Function urlPageLeave
  ${NSD_GetText} $TextField $InputValue  ; Get the URL from the input field

  ; Run PowerShell command synchronously and capture the result
  nsExec::ExecToStack '"powershell.exe" -Command "(Invoke-WebRequest -Uri $InputValue -UseBasicParsing -ErrorAction Stop).StatusCode"'
  Pop $0  ; Get the HTTP status code from PowerShell

  ; If PowerShell fails (exit code != 0), abort installation
  IfErrors AbortInstallation

  ; Check if the status code is 200 (success)
  StrCmp $0 "200" 0 ProceedWithInstallation

  ; If it's not 200, abort installation
  AbortInstallation:
    MessageBox MB_ICONEXCLAMATION "The URL entered is not accessible. Please enter a valid URL."
    Abort  ; Stop the installation process

  ; Continue the installation if URL is valid
  ProceedWithInstallation:
    ExpandEnvStrings $LocalAppDir "$PROGRAMFILES64\CentralHub"
    CreateDirectory "$LocalAppDir"

    FileOpen $0 "$LocalAppDir\config.ini" w
    FileWrite $0 "[Settings]$\r$\nCMS_URL=$InputValue$\r$\n"
    FileClose $0

    Return  ; Return after processing the valid URL

FunctionEnd

Section "Install"
    WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

Section "Uninstall"
  DeleteRegValue HKCU "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" "Shell"
  ExpandEnvStrings $LocalAppDir "$PROGRAMFILES64\CentralHub"

  IfFileExists "$LocalAppDir\config.ini" 0 +2
  Delete "$LocalAppDir\config.ini"
SectionEnd

Page custom urlPageCreate urlPageLeave
