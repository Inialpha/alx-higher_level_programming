#!/usr/bin/node

const arg = process.argv[2];
const argint = parseInt(arg);
if (isNaN(argint)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argint; i++) {
    let row = '';
    for (let j = 0; j < argint; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
