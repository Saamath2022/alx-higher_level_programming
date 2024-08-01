#!/usr/bin/env node

const fs = require('fs');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  console.log(data);
});
