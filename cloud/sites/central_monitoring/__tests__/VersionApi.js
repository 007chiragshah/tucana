import handler from '../pages/api/version';

describe('API Route: /api/version', () => {
  afterEach(() => {
    // Clean up the environment variable after each test
    delete process.env.SIBEL_VERSION;
  });

  let mockReq;
  let mockRes;

  beforeEach(() => {
    mockReq = {};
    mockRes = {
      status: jest.fn().mockReturnThis(),
      json: jest.fn(),
    };
  });

  it('should return the version from the environment variable when SIBEL_VERSION is set', () => {
    // Set the environment variable
    process.env.SIBEL_VERSION = '1.0';

    // Call the handler
    handler(mockReq, mockRes);

    // Assertions
    expect(mockRes.status).toHaveBeenCalledWith(200);
    expect(mockRes.json).toHaveBeenCalledWith({ SIBEL_VERSION: '1.0' });
  });

  it('should return "local" as the version when SIBEL_VERSION is not set', () => {
    // Unset the environment variable
    delete process.env.SIBEL_VERSION;

    // Call the handler
    handler(mockReq, mockRes);

    // Assertions
    expect(mockRes.status).toHaveBeenCalledWith(200);
    expect(mockRes.json).toHaveBeenCalledWith({ SIBEL_VERSION: 'local' });
  });
});
