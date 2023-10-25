#!/snap/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.error('Provide API URL...');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  if (!films) {
    console.error(error);
    return;
  }
  /* const uri = 'https://swapi-api.alx-tools.com/api/people/18/'; */
  const count = films.filter(film =>
    film.characters.some(characterUrl => characterUrl.endsWith('18/'))
  );
  console.log(count.length);
});
