// Generate fresh local-only credentials on a new device. Never overwrite an env file.
import { readFile, writeFile } from 'node:fs/promises';
import { randomBytes } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { resolve, dirname } from 'node:path';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const secret = randomBytes(48).toString('hex');
const api = (await readFile(resolve(root, 'apps/api/.env.example'), 'utf8'))
  .replace(/^DATABASE_URL=.*$/m, 'DATABASE_URL="postgresql://postgres:postgres@127.0.0.1:55435/template1"')
  .replace(/^AUTH_JWT_SECRET=.*$/m, `AUTH_JWT_SECRET="${secret}"`)
  .replace(/^WEB_ORIGIN=.*$/m, 'WEB_ORIGIN="http://localhost:5000"')
  .replace(/^API_PUBLIC_URL=.*$/m, 'API_PUBLIC_URL="http://localhost:5000"');
const web = (await readFile(resolve(root, 'apps/web/.env.example'), 'utf8'))
  .replace(/^NEXT_PUBLIC_SITE_URL=.*$/m, 'NEXT_PUBLIC_SITE_URL="http://localhost:5000"');
for (const [path, content] of [['apps/api/.env', api], ['apps/web/.env.local', web]]) {
  try {
    await writeFile(resolve(root, path), content, { flag: 'wx' });
    console.log('Created ' + path);
  } catch (error) {
    if (error.code !== 'EEXIST') throw error;
    console.log('Kept existing ' + path);
  }
}
