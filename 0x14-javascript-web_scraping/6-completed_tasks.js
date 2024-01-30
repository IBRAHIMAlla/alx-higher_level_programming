#!/usr/bin/node

const re = require('request');
const u = process.argv[2];

re(u, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const cop = {};
    const tk = JSON.parse(body);
    for (const m in tk) {
      const ts = tk[m];
      if (ts.completed === true) {
        if (cop[ts.userId] === undefined) {
          cop[ts.userId] = 1;
        } else {
          cop[ts.userId]++;
        }
      }
    }
    console.log(cop);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
