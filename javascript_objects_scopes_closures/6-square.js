#!/usr/bin/node

const SquareBase = require('./5-square.js');

class Square extends SquareBase {
  charPrint (c = 'X') {
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}

module.exports = Square;
