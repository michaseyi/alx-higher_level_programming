#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request.get(process.argv[2]).on('response', (res) => {
  const file = fs.createWriteStream(process.argv[3], { encoding: 'utf-8' });
  res.on('data', (chunk) => {
    file.write(chunk);
  });
  res.on('end', () => {
    file.close();
  });
});
