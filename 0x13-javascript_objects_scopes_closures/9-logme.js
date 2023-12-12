#!/usr/bin/node
let digit = 0;

exports.logMe = function (item) {
  console.log(`${digit}: ${item}`);
  digit++;
};
