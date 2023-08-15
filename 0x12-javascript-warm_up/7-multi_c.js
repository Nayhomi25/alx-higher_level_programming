#!/usr/bin/node
const x = parseInt(process.argv[2]);
let text;
if (isNaN(x)) {
  text = 'Missing number of occurrences';
  console.log(text);
} else {
  text = 'C is fun';
  let i;
  for (i = 0; i < x; i++) {
    console.log(text);
  }
}
