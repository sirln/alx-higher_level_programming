#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (process.argv.length <= 2) {
  console.error('Provide a Movie ID...');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  const data = JSON.parse(body);
  if (error) {
    console.error(error);
  } else {
    console.log(data.title);
  }
});
