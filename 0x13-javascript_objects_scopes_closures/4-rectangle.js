#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(h) && Number.isInteger(w) && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let y = '';
      for (let j = 0; j < this.width; j++) {
        y += 'X';
      }
      console.log(y);
    }
  }

  rotate () {
    const i = this.width;
    this.width = this.height;
    this.height = i;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
