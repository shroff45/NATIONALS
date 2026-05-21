const fs = require('fs');
const pkgPath = 'nyayasahayak-main-main/package.json';
const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
pkg.scripts.lint = pkg.scripts.lint.replace('--ext ts,tsx ', '');
fs.writeFileSync(pkgPath, JSON.stringify(pkg, null, 4));
