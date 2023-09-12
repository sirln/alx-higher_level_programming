#!/usr/bin/node
// Defining the Rectangle class

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let l = 0; l < this.height; l++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    if (this.width && this.height) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if (this.width && this.height) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
