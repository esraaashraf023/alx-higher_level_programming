#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const filmsWithWedge = data.results.filter(film => film.characters.find(char => char.includes('18')));
  console.log(filmsWithWedge.length);
});
