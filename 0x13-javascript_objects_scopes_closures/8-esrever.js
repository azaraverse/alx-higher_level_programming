#!/usr/bin/node

exports.esrever = function (list) {
  const final = list.length - 1;
  const array = [];
  let i = final;
  while (i >= 0) {
    array.push(list[i]);
    i--;
  }
  return array;
};
