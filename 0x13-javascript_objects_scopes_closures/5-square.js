#!/usr/bin/node
// Defining a Square class inheritting from Rectangle class

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
