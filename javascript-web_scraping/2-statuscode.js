#!/usr/bin/node

const request = require('request');

if (process.argv.length === 2) {
  console.error('please provide at least one argument');
  process.exit(1);
}

const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }
  console.log('code:', response && response.statusCode);
});
