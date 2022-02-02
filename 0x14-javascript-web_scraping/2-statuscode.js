#!/usr/bin/node
// Write a script that display the status code of a GET request.

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.error(err);
  }

  console.log('code:', response.statusCode);
});
