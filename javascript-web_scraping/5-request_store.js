#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length === 3) {
  console.error('please provide at least two arguments');
  process.exit(1);
}

const url = process.argv[2];
const fileName = process.argv[3];

request
  .get(url)
  .on('error', function (err) {
    console.error(err);
  })
  .pipe(fs.createWriteStream(fileName));
