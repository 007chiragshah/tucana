import { PatientGender } from './patient';
import { SENSOR_TYPES } from './sensor';

export interface Emulator {
  name: string;
  currentMode: string;
  modes: string[];
}

export interface EmulatorSensor {
  id: string;
  primaryIdentifier: string;
  type: SENSOR_TYPES;
  emulators: Emulator[];
}

export interface ServerEmulator {
  name: string;
  current_mode: string;
  emulation_modes: string[];
}

export interface ServerEmulatorSensor {
  id: string;
  primary_identifier: string;
  type: SENSOR_TYPES;
  emulators: ServerEmulator[];
}

export interface EmulatorUpdateEmulatorModes {
  name: string;
  mode: string;
}

export interface EmulatorUpdatedSensorModes {
  id: string;
  emulators: EmulatorUpdateEmulatorModes[];
}

export interface EmulatorPatient {
  primaryIdentifier: string;
  givenName: string;
  familyName: string;
  gender: PatientGender;
  birthDate: string;
}

export interface EmulatorMonitor {
  primaryIdentifier: string;
  name: string;
  sensors: EmulatorSensor[];
  emulators: Emulator[];
  patient?: EmulatorPatient;
}

export interface ServerEmulatorPatient {
  primary_identifier: string;
  given_name: string;
  family_name: string;
  gender: PatientGender;
  birth_date: string;
}

export interface ServerEmulatorMonitor {
  primary_identifier: string;
  name: string;
  sensors: ServerEmulatorSensor[];
  emulators: ServerEmulator[];
  patient: ServerEmulatorPatient;
}
