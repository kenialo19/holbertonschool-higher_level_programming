#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (let j = 0; j < list.length; j++) {
    if (searchElement === list[j]) {
      i++;
    }
  }
  return i;
};
