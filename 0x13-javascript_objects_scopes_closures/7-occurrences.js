#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let kidaya = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      kidaya++;
    }
    i++;
  }
  return kidaya;
};
