#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
let numBiggest = -Infinity;
let numSecondBiggest = -Infinity;

function checkSecondBiggest (numArray) {
  if (numArray.length === 0 || numArray.length === 1) {
    return 0;
  }

  for (const num of numArray) {
    if (num > numBiggest) {
      numSecondBiggest = numBiggest;
      numBiggest = num;
    } else if (num > numSecondBiggest && num !== numBiggest) {
      numSecondBiggest = num;
    }
  }

  return numSecondBiggest;
}

console.log(checkSecondBiggest(args));
