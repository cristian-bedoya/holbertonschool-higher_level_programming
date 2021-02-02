#!/usr/bin/node
let message;
if (process.argv[2]) {
  message = process.argv[2];
  console.log(message);
} else {
  message = 'No argument';
  console.log(message);
}
