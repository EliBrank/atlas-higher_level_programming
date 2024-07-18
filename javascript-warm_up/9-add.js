#!/usr/bin/node

const args = process.argv.slice(2);
const numOne = Number(args[0]);
const numTwo = Number(args[1]);

function add (a, b) {
  console.log(a + b);
}

add(numOne, numTwo);
