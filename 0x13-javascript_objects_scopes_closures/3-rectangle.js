#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method
  print () {
    const holder = 'X';
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

module.exports = Rectangle;
