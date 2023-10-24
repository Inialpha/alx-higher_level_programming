#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (err, response, body) {
  if (err) {
    // pass
  }
  for (const film of JSON.parse(body).results) {
    const characters = film.characters;
    for (const c of characters) {
      if (c.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
