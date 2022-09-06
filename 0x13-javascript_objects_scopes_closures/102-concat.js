#!/usr/bin/node
const fs = require('fs');
const sources = [fs.createReadStream(process.argv[2]), fs.createReadStream(process.argv[3])];
const dest = fs.createWriteStream(process.argv[4]);

sources.forEach((source) => {
  source.pipe(dest);
  source.close();
});
dest.close();
