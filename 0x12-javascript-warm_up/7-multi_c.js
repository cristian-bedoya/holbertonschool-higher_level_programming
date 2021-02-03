#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  for (let step = 0; step < process.argv[2]; step++) {
    console.log('C is fun');
  }
}
