#!/usr/bin/node
// This script writes a string to a file
const fs = require('fs');
try {
  fs.writeFileSync(process.argv[2], process.argv[3], { encoding: 'utf-8' });
} catch (error) {
  console.log(error);
}
