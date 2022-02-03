#!/usr/bin/node
// Write a script that prints the number of movies where the character Wedge Antilles is present.

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const wi = JSON.parse(body).results;
    let j = 0;
    for (const X of wi) {
      for (const char of X.characters) {
        if (char.search('/18/') > 0) {
          j++;
        }
      }
    }
    console.log(j);
  }
});
