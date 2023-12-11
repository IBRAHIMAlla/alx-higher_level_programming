#!/usr/bin/node
function fact (f) {
  return f === 0 || isNaN(f) ? 1 : f * fact(f - 1);
}

console.log(fact(Number(process.argv[2])));
