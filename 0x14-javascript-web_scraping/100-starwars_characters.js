#!/usr/bin/node
const request = require('request');
function parseBody (stream) {
  return new Promise(resolve => {
    const chunks = [];
    stream.on('data', (chunk) => {
      chunks.push(chunk);
    });
    stream.on('end', () => {
      stream.body = JSON.parse(Buffer.concat(chunks));
      resolve();
    });
  });
}

request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`).on('response', async (res) => {
  await parseBody(res);
  const characters = res.body.characters;
  for (const character of characters) {
    await new Promise(resolve => {
      request.get(character).on('response', async (res) => {
        await parseBody(res);
        console.log(res.body.name);
        resolve();
      });
    });
  }
});
