#!/usr/bin/node

const m = require('fs');

const s1 = process.argv[2];
const s2 = process.argv[3];
const dt = process.argv[4];

function callback (err, data) {
  if (err) {
    return console.log(err);
  }
  m.appendFile(dt, data, function (err) {
    if (err) console.log(err);
  });
}

m.readFile(s1, 'utf8', callback);
m.readFile(s2, 'utf8', callback);
