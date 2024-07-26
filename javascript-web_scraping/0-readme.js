#!/usr/bin/node

const fs = require('fs');

if (process.argv.length === 2) {
  console.error('please provide at least one argument');
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
