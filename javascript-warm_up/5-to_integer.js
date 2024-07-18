#!/usr/bin/node

// gets user args by ignoring first 2 mandatory args
// e.g. 'node 2-arguments.js' <- these are ignored
const args = process.argv.slice(2);

const myNum = Number(args[0]);

if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNum}`);
}
