#!/usr/bin/node

const list = require('./100-data').list;

let newArr = [];
newArr = list.map(function (n, i) {
  return n * i;
});

console.log(list);
console.log(newArr);
