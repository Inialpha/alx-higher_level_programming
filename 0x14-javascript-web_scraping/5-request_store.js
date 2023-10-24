#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const file = process.argv[3];
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    // pass
  }
  fs.writeFile(file, body, 'utf8', function (err) {
    if (err) {
      // pass
    }
  });
});
