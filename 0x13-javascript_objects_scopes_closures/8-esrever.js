#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (let m = list.length - 1; m >= 0; m--) {
    rev.push(list[m]);
  }
  return rev;
};
