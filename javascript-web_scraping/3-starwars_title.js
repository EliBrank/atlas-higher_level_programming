#!/usr/bin/node

const request = require('request');

if (process.argv.length === 2) {
  console.error('please provide at least one argument');
  process.exit(1);
}

const starWarsFilmNum = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + starWarsFilmNum;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }
  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
