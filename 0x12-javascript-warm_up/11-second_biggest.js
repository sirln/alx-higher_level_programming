#!/usr/bin/node
// prints the second biggest integer in list of arguments

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log('0');
} else {
  const intArr = args.map(s => parseInt(s));
  const sortedArr = intArr.sort((a, b) => a - b);
  const setValues = new Set(sortedArr);
  const sortedValues = Array.from(setValues);
  console.log(sortedValues[sortedValues.length - 2]);
}
