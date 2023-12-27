#!/usr/bin/node
const numArg = process.argv.length - 2;

if (numArg === 0) {
  console.log("No argument");
} else if (numArg === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
