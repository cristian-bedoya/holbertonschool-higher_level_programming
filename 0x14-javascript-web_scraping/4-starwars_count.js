#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    let counter = 0;
    const arrayresults = JSON.parse(body).results;
    const character18 = 'https://swapi-api.hbtn.io/api/people/18/'
    for (let movie of arrayresults) {
      const chars = movie.characters;
      if (chars.includes(character18)) {
        counter ++;
      }
      }
    console.log(counter);
  }
});
