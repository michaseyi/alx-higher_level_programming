#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];

  list.forEach((listItem) => {
    reversedList.unshift(listItem);
  });

  return reversedList;
};
