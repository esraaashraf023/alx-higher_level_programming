#!/usr/bin/node

const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const data = JSON.parse(body);
  data.characters.map(character => {
    request.get(character, (err, res, body) => {
      if (err) {
        return console.log(err);
      } else {
        const name = JSON.parse(body).name;
        console.log(name);
      }
    });
    return 0;
  });
});
