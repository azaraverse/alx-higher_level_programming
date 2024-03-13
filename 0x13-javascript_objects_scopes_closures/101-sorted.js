#!/usr/bin/node

const dict = require('./101-data').dict;

const ids = {};

// iterate over each id and occurrence
for (const id in dict) {
  const occurrence = dict[id];
  /*
    if the occurrence isn't a key in the new dictionary, yet
    create it with an array containing the current id as its value
    */
  if (!(occurrence in ids)) {
    ids[occurrence] = [id];
  } else {
    ids[occurrence].push(id);
  }
}

console.log(ids);
