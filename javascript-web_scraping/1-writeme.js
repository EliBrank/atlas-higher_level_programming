#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 3) {
  console.error('please provide at least two arguments');
  process.exit(1);
}

const filePath = process.argv[2];
const userString = process.argv[3];

fs.writeFile(filePath, userString, 'utf8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
});
