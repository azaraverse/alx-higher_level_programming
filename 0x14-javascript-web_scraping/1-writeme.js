#!/usr/bin/node

// create fileSystem instance
const fs = require('fs');

// write a function to write string to file
function writeFile (filePath, data) {
  fs.writeFile(filePath, data, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
}

const filePath = process.argv[2];
const data = process.argv[3];
writeFile(filePath, data);
