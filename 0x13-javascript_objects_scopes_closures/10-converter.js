#!/usr/bin/node
exports.converter = function (base) {
  function cnv (num) {
    return num.toString(base);
  }
  return cnv;
};
