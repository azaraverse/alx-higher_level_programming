#!/usr/bin/node
const myVar = 'X';
const argvHolder = parseInt(process.argv[2]);

if (isNaN(argvHolder)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < argvHolder) {
    let str = '';
    let j = 0;
    while (j < argvHolder) {
      str += myVar;
      j++;
    }
    console.log(str);
    i++;
  }
}
