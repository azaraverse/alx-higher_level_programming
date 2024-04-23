#!/usr/bin/node

// create request instance
const request = require('request');

// function to print all characters of a Starwars movie
function printCharacters (filmId) {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId + '/';
  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.log(err);
    } if (response.statusCode !== 200) {
      console.log('code:', response.statusCode);
    } else {
      const data = JSON.parse(body);
      const characterUrls = data.characters;

      for (const charUrl of characterUrls) {
        request.get(charUrl, (err, response, body) => {
          if (err) {
            console.log(err);
          } if (response.statusCode !== 200) {
            console.log('code:', response.statusCode);
          } else {
            const charData = JSON.parse(body);
            console.log(charData.name);
          }
        });
      }
    }
  });
}

// store film id in a variable
const filmId = process.argv[2];

// call function and pass variable as argument
printCharacters(filmId);
