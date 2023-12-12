#!/usr/bin/node
exports.converter = function (base) {
  function cnv (number) {
    return number.toString(base);
  }
  return cnv;
};
