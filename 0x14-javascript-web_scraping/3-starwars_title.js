#!/usr/bin/node

// create request module instance
const request = require('request');

// function to get title from api
function getTitle (filmId) {
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;
  request.get(apiUrl, (err, response, body) => {
    if (err) {
      console.log(err);
    } if (response.statusCode !== 200) {
      console.log('code:', response.statusCode);
    } else {
      const film = JSON.parse(body);
      console.log(film.title);
    }
  });
}

// store id in a variable
const filmId = process.argv[2];

// call function to accept variable (id)
getTitle(filmId);
