#!/usr/bin/node

// create fileSystem instance
const fs = require('fs');
const request = require('request');

// write a function to write string to file
function writeWebPage (urlPath, filePath) {
  request.get(urlPath, (err, response, body) => {
    if (err) {
      console.log(err);
    } if (response.statusCode !== 200) {
      console.log('code:', response.statusCode);
    } else {
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}

const urlPath = process.argv[2];
const filePath = process.argv[3];
writeWebPage(urlPath, filePath);
