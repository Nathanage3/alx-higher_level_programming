#!/usr/bin/node
// executes x times a function.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
