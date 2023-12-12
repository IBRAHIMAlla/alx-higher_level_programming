#!/usr/bin/node
const SquareModel = require('./5-square');

module.exports = class Square extends SquareModel {
  constructor (z) {
    super(z, z);
  }

  charPrint (c) {
    this.print(c);
  }
};
