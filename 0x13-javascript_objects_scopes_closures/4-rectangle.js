#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const i = 'X';
    for (let j = 0; j < this.height; j++) {
      console.log(i.repeat(this.width));
    }
  }

  rotate () {
    const exchange = this.width;
    this.width = this.height;
    this.height = exchange;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
