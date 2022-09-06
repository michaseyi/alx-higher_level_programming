#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (number === 0) return '0';

    function convertNumber (number, convertedNumber, alphabets) {
      if (number === 0) return convertedNumber;

      if (number % base < 10) {
        return convertNumber(Math.floor(number / base), (number % base) + convertedNumber, alphabets);
      }
      return convertNumber(Math.floor(number / base), alphabets[(number % base) - 10] + convertedNumber, alphabets);
    }

    return convertNumber(number, '', 'abcdef');
  };
};
