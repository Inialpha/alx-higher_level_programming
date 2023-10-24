#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const file = args[2];

fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
