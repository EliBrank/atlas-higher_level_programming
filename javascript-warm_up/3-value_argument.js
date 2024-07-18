#!/usr/bin/node

// gets user args by ignoring first 2 mandatory args
// e.g. 'node 2-arguments.js' <- these are ignored
const args = process.argv.slice(2);

if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
