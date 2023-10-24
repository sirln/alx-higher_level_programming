#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (process.argv.length <= 2) {
  console.error('Provide a url...');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
