#!/usr/bin/node
// importing a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence

const { dict } = require('./101-data.js');

const newDict = {};
for (const userId in dict) {
  const occurrence = dict[userId];

  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }

  newDict[occurrence].push(userId);
}

console.log(newDict);
