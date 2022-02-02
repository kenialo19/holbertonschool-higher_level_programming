#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (err, response, body) {
  if (err) {
    return console.error(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
