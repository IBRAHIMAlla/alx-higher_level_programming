#!/usr/bin/node
const lt = require('./100-data').list;
const ma = lt.map(function (v, m) { return v * m; });
console.log(lt);
console.log(ma);
