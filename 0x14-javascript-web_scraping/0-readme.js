#!/usr/bin/node

// create fileSystem instance
const fs = require('fs');

// write a function to read and print file content to console
function readPrintFile (filePath) {
  fs.readFile(filePath, 'utf-8', (data, err) => {
    if (err) {
      console.log(err);
    } if (data) {
      console.log(data);
    }
  });
}

const filePath = process.argv[2];
readPrintFile(filePath);
