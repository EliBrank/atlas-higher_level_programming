#!/usr/bin/node

const statement = 'C is fun';
const args = process.argv.slice(2);
const myNum = args[0];

if (args[0] === undefined) {
  console.log('Missing number of occurrences');
} else if (myNum > 0) {
  for (let i = 0; i < myNum; i++) {
    console.log(statement);
  }
}
