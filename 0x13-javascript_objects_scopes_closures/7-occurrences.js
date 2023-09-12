#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const item of list) {
    if (item === searchElement) {
      count++;
    }
  }
  return (count);
};
