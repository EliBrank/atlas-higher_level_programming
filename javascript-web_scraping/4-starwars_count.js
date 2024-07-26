#!/usr/bin/node

const request = require('request');

if (process.argv.length === 2) {
  console.error('please provide at least one argument');
  process.exit(1);
}

const url = process.argv[2];
const characterID = '18';

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const films = JSON.parse(body);
    let appearenceCount = 0;
    for (const film of films.results) {
      for (const char of film.characters) {
        if (char.endsWith(`/${characterID}/`)) {
          appearenceCount++;
        }
      }
    }
    console.log(appearenceCount);
  }
});
