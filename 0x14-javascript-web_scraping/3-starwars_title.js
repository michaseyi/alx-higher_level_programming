#!/usr/bin/node
// This script prints the title of a Star Wars movie where the episode
// number matches a given integer
const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`).on('response', (res) => {
  const chunks = [];
  res.on('data', (chunk) => {
    chunks.push(chunk);
  });
  res.on('end', () => {
    const body = JSON.parse(Buffer.concat(chunks));
    console.log(body.title);
  });
});
