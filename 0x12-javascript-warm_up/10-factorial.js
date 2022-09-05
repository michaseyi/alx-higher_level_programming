#!/usr/bin/node
const number = Number(process.argv[2]);
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}

function factorial (number) {
  if (number === 0) {
    return 1;
  }
  return number * factorial(number - 1);
}
