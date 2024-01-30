#!/usr/bin/node
const m = require('fs');
const re = require('request');
re(process.argv[2]).pipe(m.createWriteStream(process.argv[3]));
