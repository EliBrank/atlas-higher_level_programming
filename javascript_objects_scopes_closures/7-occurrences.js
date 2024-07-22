#!/usr/bin/node

function nbOccurences (listToCheck = [], searchTerm) {
  let searchMatches = 0;
  for (const item of listToCheck) {
    if (item === searchTerm) {
      searchMatches++;
    }
  }

  return searchMatches;
}

module.exports = { nbOccurences };
