#!/usr/bin/node

function converter (base) {
  return function (input) {
    return (input.toString(base));
  };
}

module.exports = { converter };
