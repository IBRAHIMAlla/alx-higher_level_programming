#!/usr/bin/node
const lt = require('./101-data').dict;
const s = {};

Object.keys(lt).forEach(key => {
  if (s[lt[key]] === undefined) s[lt[key]] = [];
  s[lt[key]].push(key);
}
);
console.log(s);
