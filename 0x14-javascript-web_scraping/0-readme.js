#!/usr/bin/node
const m = require('fs');
m.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
