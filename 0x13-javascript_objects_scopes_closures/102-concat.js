#!/usr/bin/node
const fs = require('fs');

const sources = [
  fs.readFileSync(process.argv[2]),
  fs.readFileSync(process.argv[3])
];
fs.writeFileSync(process.argv[4], sources.join(''));
