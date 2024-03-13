#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method print
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

  // instance method double
  double () {
    this.width *= 2;
    this.height *= 2;
  }

  // instance method rotate
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
}

module.exports = Rectangle;
