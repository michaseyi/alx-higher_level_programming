#!/usr/bin/node

exports.logMe = (function () {
  let logCount = 0;
  return function (item) {
    console.log(`${logCount}: ${item}`);
    logCount += 1;
  };
})();
