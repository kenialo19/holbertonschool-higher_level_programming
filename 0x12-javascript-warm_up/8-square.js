#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let y = 0; y < x; y++) {
    console.log('X'.repeat(x));
  }
}
