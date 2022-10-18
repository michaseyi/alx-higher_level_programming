#!/usr/bin/node
const request = require('request');
request.get(process.argv[2]).on('response', (res) => {
  const chunks = [];
  res.on('data', (chunk) => {
    chunks.push(chunk);
  });
  res.on('end', () => {
    const body = JSON.parse(Buffer.concat(chunks));
    const count = body.results.reduce((total, curr) => {
      const characters = curr.characters;
      if (characters.includes('https://swapi-api.hbtn.io/api/people/18/')) return total + 1;
      return total;
    }, 0);
    console.log(count);
  });
});
