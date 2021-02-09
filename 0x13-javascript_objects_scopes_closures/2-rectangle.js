#!/usr/bin/node
class Rectangle {
  constructor(h, w) {
    if (Number.isInteger(h) && Number.isInteger(w) && h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }
}
module.exports = Rectangle;
