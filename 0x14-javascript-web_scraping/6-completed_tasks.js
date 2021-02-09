#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const dicttask = {};
    const elements = JSON.parse(body);
    for (const i of elements) {
      if (i.completed) {
        if (!dicttask[i.userId]) {
          dicttask[i.userId] = 1;
        } else {
          dicttask[i.userId] += 1;
        }
      }
    }
    console.log(dicttask);
  }
});
