#!/usr/bin/node

// gets user args by ignoring first 2 mandatory args
// e.g. 'node 2-arguments.js' <- these are ignored
const args = process.argv.slice(2);

console.log(`${args[0]} is ${args[1]}`);
