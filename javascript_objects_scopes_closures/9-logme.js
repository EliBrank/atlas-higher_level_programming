#!/usr/bin/node

let logCount = 0;

function logMe (item) {
  logCount++;
  console.log(`${logCount}: ${item}`);
}

module.exports = { logMe };
