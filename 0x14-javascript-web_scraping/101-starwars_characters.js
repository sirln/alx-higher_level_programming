#!/usr/bin/node

const movieId = process.argv[2];
const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (process.argv.length <= 2) {
  console.error('Provide Movie ID...');
  process.exit(1);
}

function fetchCharacterName (urls, index) {
  if (index >= urls.length) {
    process.exit(0);
  }

  request.get(urls[index], (err, res, charBody) => {
    if (err) {
      console.error(err);
    }
    const character = JSON.parse(charBody);
    console.log(character.name);

    fetchCharacterName(urls, index + 1);
  });
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  fetchCharacterName(film.characters, 0);
});
