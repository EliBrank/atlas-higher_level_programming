#!/usr/bin/node

const args = process.argv.slice(2);
const myNum = Number(args[0]);

function factorial (num) {
  if (isNaN(num)) {
    num = 1;
  }
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(myNum));
