#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, function (err, response, body) {
  if (err) {
    // pass
  }

  const characters = JSON.parse(body).characters;
  for (let index = 0; index < characters.length; index++) {
    request(characters[index], function (err, response, body) {
      if (err) {
        //
      }
      console.log(JSON.parse(body).name);
    });
  }
});
