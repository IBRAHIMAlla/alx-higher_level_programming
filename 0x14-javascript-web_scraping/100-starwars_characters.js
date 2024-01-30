#!/usr/bin/node

const rr = require('request');
const dd = process.argv[2];
const uu = 'https://swapi-api.hbtn.io/api/films/';
rr.get(uu + dd, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const dtt = JSON.parse(body);
  const gg = dtt.characters;
  for (const m of gg) {
    rr.get(m, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const dtt1 = JSON.parse(body1);
      console.log(dtt1.name);
    });
  }
});
