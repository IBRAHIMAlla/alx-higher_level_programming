#!/usr/bin/node
const z = Math.floor(Number(process.argv[2]));
if (isNaN(z)) {
  console.log('Missing size');
} else {
  for (let w = 0; w < z; w++) {
    let r = '';
    for (let m = 0; m < z; m++) r += 'X';
    console.log(r);
  }
}
