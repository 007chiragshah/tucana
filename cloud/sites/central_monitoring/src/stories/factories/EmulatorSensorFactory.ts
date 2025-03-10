import { Emulator, EmulatorSensor } from '@/types/emulator';
import { SENSOR_TYPES } from '@/types/sensor';
import { faker } from '@faker-js/faker';

export const createEmulator = (override: Partial<Emulator> = {}): Emulator => {
  const modes = ['low', 'normal', 'high'];
  return {
    name: faker.lorem.word(),
    currentMode: faker.helpers.arrayElement(modes),
    modes,
    ...override,
  };
};

export const createEmulatorSensor = (override: Partial<EmulatorSensor> = {}): EmulatorSensor => ({
  id: faker.string.uuid(),
  primaryIdentifier: faker.string.uuid(),
  type: faker.helpers.arrayElement(Object.values(SENSOR_TYPES)),
  emulators: faker.helpers.multiple(createEmulator, { count: 5 }),
  ...override,
});
