#!/usr/bin/node
let str1;
const str2 = 'undefined';
const str3 = 'is';
const leng1 = process.argv.length;
if (leng1 === 3) {
  str1 = [process.argv[2], str3, str2];
  console.log(str1.join(' '));
} else if (leng1 === 4) {
  str1 = [process.argv[2], str3, process.argv[3]];
  console.log(str1.join(' '));
} else {
  str1 = [str2, str3, str2];
  console.log(str1.join(' '));
}
