#!/usr/bin/node
// This script opens the file cisfun and prints out the contents
const fs = require('fs');
try {
  const data = fs.readFileSync(process.argv[2], { encoding: 'utf-8' });
  console.log(data);
} catch (error) {
  console.log(error);
}
