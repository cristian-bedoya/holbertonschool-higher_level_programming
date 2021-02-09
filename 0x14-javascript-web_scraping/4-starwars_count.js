#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    let counter = 0;
    const arrayresults = JSON.parse(body).results;
    const id18 = '18';
    for (const movies of arrayresults) {
      const chars = movies.characters;
      for (const list of chars) {
        if (list.includes(id18)) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
