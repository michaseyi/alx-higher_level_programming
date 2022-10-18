#!/usr/bin/node
// This script display the statuc code of a GET request
const request = require('request');
request.get(process.argv[2]).on('response', (res) => {
  console.log(`code: ${res.statusCode}`);
});
