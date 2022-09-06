#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

Object.keys(dict).forEach((key) => {
  if (!(dict[key] in newDict)) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
});
