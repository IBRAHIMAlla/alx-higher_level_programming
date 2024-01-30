#!/usr/bin/node
const rr = require('request');
const uu = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
rr(uu, function (error, response, body) {
  if (!error) {
    const chrr = JSON.parse(body).characters;
    printCharacters(chrr, 0);
  }
});

function printCharacters (chrr, index) {
  rr(chrr[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chrr.length) {
        printCharacters(chrr, index + 1);
      }
    }
  });
}
