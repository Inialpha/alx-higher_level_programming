#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, function (err, response, body) {
  console.log(err || JSON.parse(body).title);
});
