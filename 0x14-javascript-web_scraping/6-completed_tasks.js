#!/usr/bin/node
const request = require('request');
request.get(process.argv[2]).on('response', (res) => {
  const chunks = [];
  res.on('data', (chunk) => {
    chunks.push(chunk);
  });
  res.on('end', () => {
    const tasks = JSON.parse(Buffer.concat(chunks));
    const data = {};
    tasks.forEach(task => {
      if (task.completed) {
        if (data[task.userId] !== undefined) {
          data[task.userId]++;
        } else {
          data[task.userId] = 1;
        }
      }
    });
    console.log(data);
  });
});
