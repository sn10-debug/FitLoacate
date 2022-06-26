'use strict';

let word1 = prompt('Enter the Word 1');
let word2 = prompt('Enter the Word 2');
let words = [];
word_Checker = function (word) {
  let word_sample = [];
  word_new = word
    .split('')
    .map(mov => {
      if (word_sample.includes(mov)) return;
      word_sample.push(mov);
      return mov;
    })
    .filter(mov => mov);

  words.push(word_new.join(''));
};
word_Checker(word1);
word_Checker(word2);
console.log(words);
let array1 = new Array(8);
array1.fill(1, 0, 8);
