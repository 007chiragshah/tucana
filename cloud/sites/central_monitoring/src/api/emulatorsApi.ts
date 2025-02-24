import {
  Emulator,
  EmulatorMonitor,
  EmulatorSensor,
  ServerEmulator,
  ServerEmulatorMonitor,
  ServerEmulatorPatient,
  ServerEmulatorSensor,
} from '@/types/emulator';

const parseEmulatorData = (rawEmulator: ServerEmulator) => {
  return {
    name: rawEmulator.name,
    currentMode: rawEmulator.current_mode,
    modes: rawEmulator.emulation_modes,
  };
};

const parseEmulatorsData = (rawEmulators: ServerEmulator[]) => {
  const res: Emulator[] = [];
  rawEmulators.forEach((rawEmulator) => {
    res.push(parseEmulatorData(rawEmulator));
  });
  return res;
};

const parseSensorData = (rawSensor: ServerEmulatorSensor) => {
  return {
    id: rawSensor.id,
    primaryIdentifier: rawSensor.primary_identifier,
    type: rawSensor.type,
    emulators: parseEmulatorsData(rawSensor.emulators),
  };
};

const parseSensorsData = (rawSensors: ServerEmulatorSensor[]) => {
  const res: EmulatorSensor[] = [];
  rawSensors.forEach((rawSensor) => {
    res.push(parseSensorData(rawSensor));
  });
  return res;
};

const parseEmulatedPatientData = (rawPatient: ServerEmulatorPatient) => {
  if (rawPatient) {
    return {
      primaryIdentifier: rawPatient.primary_identifier,
      givenName: rawPatient.given_name,
      familyName: rawPatient.family_name,
      gender: rawPatient.gender,
      birthDate: rawPatient.birth_date,
    };
  }
  return undefined;
};

const parseMonitorData = (rawMonitor: ServerEmulatorMonitor): EmulatorMonitor => {
  return {
    primaryIdentifier: rawMonitor.primary_identifier,
    name: rawMonitor.name,
    sensors: parseSensorsData(rawMonitor.sensors),
    emulators: parseEmulatorsData(rawMonitor.emulators),
    patient: parseEmulatedPatientData(rawMonitor.patient),
  };
};

export const parseEmulatedMonitorData = (rawMonitors: ServerEmulatorMonitor[]) => {
  const res: EmulatorMonitor[] = [];
  rawMonitors.forEach((rawMonitors) => {
    res.push(parseMonitorData(rawMonitors));
  });
  return res;
};
