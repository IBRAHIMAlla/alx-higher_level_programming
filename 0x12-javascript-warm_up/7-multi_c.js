#!/usr/bin/node
const a = Math.floor(Number(process.argv[2]));
if (isNaN(a)) {
  console.log('Missing number of occurrences');
} else {
  for (let m = 0; m < a; m++) {
    console.log('C is fun');
  }
}
