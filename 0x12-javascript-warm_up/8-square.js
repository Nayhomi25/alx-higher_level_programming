#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i, j, text;
  for (i = 0; i < x; i++) {
    text = '';
    for (j = 0; j < x; j++) {
      text += 'X';
    }
    console.log(text);
  }
}
