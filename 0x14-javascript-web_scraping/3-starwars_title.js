#!/usr/bin/node

const req = require('request');
const ep = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

request(API_URL + ep, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const resp = JSON.parse(body);
    console.log(resp.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
