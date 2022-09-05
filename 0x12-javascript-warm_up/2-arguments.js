#!/usr/bin/node
if (process.argv.slice(1, -1).length > 0) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
