#!/usr/bin/node

// create request instance
const request = require('request');

// function to get & display statusCode
function getStatusCode (url) {
  request
    .get(url)
    .on('response', function (response) {
      console.log('code:', response.statusCode);
    });
}

const url = process.argv[2];
getStatusCode(url);
