#!/usr/bin/node
const myVar = 'C is fun';
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log(myVar);
    i++;
  }
}
