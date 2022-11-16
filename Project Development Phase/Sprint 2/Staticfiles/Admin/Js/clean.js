const sh = require('shelljs');
const upath = require('upath');

const destPath = upath.resolve(upath.dirname(__filename), '../dist');

sh.rm('-rf', `${destPath}/*`)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
