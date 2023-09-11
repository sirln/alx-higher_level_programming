#!/usr/bin/node
// prints a square, size of first arg

const s = process.argv[2];
let index;

if (isNaN(s)) {
  console.log('Missing size');
} else {
  for (index = s; index > 0; index--) {
    console.log('X'.repeat(s));
  }
}
