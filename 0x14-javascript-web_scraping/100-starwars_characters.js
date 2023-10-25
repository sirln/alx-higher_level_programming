#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (process.argv.length <= 2) {
  console.error('Provide Movie ID...');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const characterUrls = film.characters;

  characterUrls.forEach((url, index) => {
    request.get(url, (err, res, charBody) => {
      if (err) {
        console.error(err);
      } else {
        const character = JSON.parse(charBody);
        console.log(character.name);
      }
    });
  });
});
