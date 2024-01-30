#!/usr/bin/node
const m = require('fs');
m.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
