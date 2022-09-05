#!/usr/bin/node
const firstNumber = Number(process.argv[2]);
const secondNumber = Number(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(firstNumber, secondNumber));
