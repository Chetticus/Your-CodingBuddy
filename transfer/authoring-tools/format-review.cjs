const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const prettier = require('../apps/api/node_modules/prettier');
async function main() {
  const changed = execFileSync('git', ['diff', '--name-only', '-z'], { encoding: 'utf8' });
  const added = execFileSync('git', ['ls-files', '--others', '--exclude-standard', '-z'], { encoding: 'utf8' });
  const files = [...new Set((changed + added).split('\0').filter(Boolean))].filter(f => fs.existsSync(f) && /\.(tsx?|css|[cm]js)$/.test(f));
  for (const file of files) {
    const source = fs.readFileSync(file, 'utf8');
    const config = await prettier.resolveConfig(file);
    const formatted = await prettier.format(source, { ...config, filepath: path.resolve(file) });
    if (formatted !== source) fs.writeFileSync(file, formatted);
  }
  console.log('Formatted ' + files.length + ' changed source files.');
}
main().catch(error => { console.error(error); process.exitCode = 1; });
