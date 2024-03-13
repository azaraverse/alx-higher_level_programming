#!/usr/bin/node

const newSquare = require('./5-square');

class Square extends newSquare {
  // instance method charPrint
  charPrint (c) {
    let holder = c;
    if (holder === undefined) {
      holder = 'X';
    }
    let i = 0;
    while (i < this.height) {
      let str = '';
      let j = 0;
      while (j < this.width) {
        str += holder;
        j++;
      }
      console.log(str);
      i++;
    }
  }
}

module.exports = Square;
