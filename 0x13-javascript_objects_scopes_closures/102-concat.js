#!/usr/bin/node
// script that concats 2 files

const args = process.argv.slice(2);
const file = require("fs");
const contentA = file.readFileSync("./" + args[0]);
const contentB = file.readFileSync("./" + args[1]);
file.writeFileSync("./" + args[2], contentA + contentB);
