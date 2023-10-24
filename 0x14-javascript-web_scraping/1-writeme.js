#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

if (process.argv.length <= 3) {
  console.error('Provide file path and a string to write.');
  process.exit(1);
}

fs.writeFile(filePath, string, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
