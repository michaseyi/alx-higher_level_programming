#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrenceCount = 0;

  list.forEach((currentValue) => {
    if (currentValue === searchElement) {
      occurrenceCount += 1;
    }
  });
  return occurrenceCount;
};
