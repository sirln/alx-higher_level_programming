#!/usr/bin/node

const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');

if (process.argv.length <= 3) {
  console.error('Provide a URL and file path respectively...');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
