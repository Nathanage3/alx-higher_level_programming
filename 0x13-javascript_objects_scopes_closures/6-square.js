#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const SquareBase = require("./5-square");

class Square extends SquareBase {
  charPrint(c) {
    if (c === undefined) {
      c = "X";
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
