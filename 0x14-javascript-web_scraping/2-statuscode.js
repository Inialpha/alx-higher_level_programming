#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    // pass
  }

  console.log(`code: ${response.statusCode}`);
});
