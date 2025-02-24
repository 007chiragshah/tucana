import { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  res.status(200).json({ SIBEL_VERSION: process.env.SIBEL_VERSION || 'local' });
}
