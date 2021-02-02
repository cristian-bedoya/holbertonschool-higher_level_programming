#!/usr/bin/node
let message;
const leng1 = process.argv.length;
if (leng1 < 3) {
  message = 'No argument';
  console.log(message);
} else if (leng1 === 3) {
  message = 'Argument found';
  console.log(message);
} else {
  message = 'Arguments found';
  console.log(message);
}
