#!/usr/bin/node
//  new function incr that increments the integer value.

const myObject = {
  type: "object",
  value: 12,
};
console.log(myObject);
myObject.incr = function () {
  myObject.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
