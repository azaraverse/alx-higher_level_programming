#!/usr/bin/node

// create request module instance
const request = require('request');

// function to get number od movies where character ID 18 is present from api
function getTitle (apiUrl, characterId) {
  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.log(err);
    } if (response.statusCode !== 200) {
      console.log('code:', response.statusCode);
    } else {
      const films = JSON.parse(body).results;
      let count = 0;
      for (const film of films) {
        if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/' + characterId + '/')) {
          count++;
        }
      }
      console.log(count);
    }
  });
}

// store id in a variable
const apiUrl = process.argv[2];

// call function to accept variable (id)
getTitle(apiUrl, 18);
