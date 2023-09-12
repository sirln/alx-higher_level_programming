#!/usr/bin/node
// Defining a Square class inheritting from Square class

const ParentSquare = require('./5-square.js');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let l = 0; l < this.height; l++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
