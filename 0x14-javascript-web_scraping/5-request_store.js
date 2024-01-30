#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
    if (err) console.log(err);
  });
});
