#!/usr/bin/node

function factorial (a) {
  return (a === 0 || isNaN(a) ? 1 : a * factorial(a - 1));
}
const fac = factorial(Number(process.argv[2]));
console.log(fac);
