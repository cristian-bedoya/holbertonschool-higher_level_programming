#!/usr/bin/node
class Rectangle {
  constructor (h, w) {
    if (Number.isInteger(h) && Number.isInteger(w) && h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.width; i++) {
      let y = '';
      for (let j = 0; j < this.height; j++) {
        y += 'X';
      }
      console.log(y);
    }
  }
}
module.exports = Rectangle;
