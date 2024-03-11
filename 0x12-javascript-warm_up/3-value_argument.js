#!/usr/bin/node
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  const holder = process.argv[2];
  console.log(holder);
}
