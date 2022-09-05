#!/usr/bin/node

function secondBiggest (array) {
  if (array.length < 2) {
    console.log(0);
  } else {
    array.sort((a, b) => b - a);
    console.log(array[1]);
  }
}

secondBiggest(process.argv.slice(2));
