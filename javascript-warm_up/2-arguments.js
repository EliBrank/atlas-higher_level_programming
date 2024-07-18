#!/usr/bin/node

// gets user args by ignoring first 2 mandatory args
// e.g. 'node 2-arguments.js' <- these are ignored
const args = process.argv.slice(2);

const numArgs = args.length;

if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found')
} else {
  console.log('Arguments found');
}
