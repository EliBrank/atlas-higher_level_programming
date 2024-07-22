#!/usr/bin/node

function esrever (listInput = []) {
  const listRev = [];
  for (const item of listInput) {
    listRev.unshift(item);
  }

  return listRev;
}

module.exports = { esrever };
