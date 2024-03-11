#!/usr/bin/node
const argvHolder = process.argv[2];

if (argvHolder === undefined) {
  console.log('No argument');
} else {
  console.log(argvHolder);
}
