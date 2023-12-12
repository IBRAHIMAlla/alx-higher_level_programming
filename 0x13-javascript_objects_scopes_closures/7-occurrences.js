#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let digit = 0;
  list.forEach(elm => {
    if (elm === searchElement) digit++;
  });
  return digit;
};
