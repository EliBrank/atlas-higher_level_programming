#!/usr/bin/node

const args = process.argv.slice(2);
const myNum = Number(args[0]);

if (isNaN(myNum)) {
  console.log('Missing size');
} else if (myNum > 0) {
  for (let i = 0; i < myNum; i++) {
    for (let j = 0; j < myNum; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
