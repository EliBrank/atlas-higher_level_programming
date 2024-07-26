#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

// this check should cover all issues with user input
if (!fs.existsSync(filePath)) {
  console.error('please provide a valid file path');
  process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
	console.error('error reading the file:', err.message);
	process.exit(1);
  }
  console.log(data);
});
