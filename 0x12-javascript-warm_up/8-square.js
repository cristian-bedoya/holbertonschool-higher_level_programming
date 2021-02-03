#!/usr/bin/node
const argPass = process.argv[2];
if (parseInt(process.argv[2])) {
  for (let i = 0; i < argPass; i++) {
    let y = '';
    for (let j = 0; j < argPass; j++) {
      y += 'X';
    }
    console.log(y);
  }
} else {
  console.log('Missing size');
}
