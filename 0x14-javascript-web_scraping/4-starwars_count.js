#!/usr/bin/node
const re = require('request');
re(process.argv[2], function (error, response, body) {
  if (!error) {
    const res = JSON.parse(body).results;
    console.log(res.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
