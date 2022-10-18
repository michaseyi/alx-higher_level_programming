#!/usr/bin/node
// This script opens the file cisfun and prints out the contents
const fs = require('fs');
const data = fs.readFileSync('cisfun', { encoding: 'utf-8' });
console.log(data);
