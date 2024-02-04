#!/usr/bin/node
const fs = require("fs");

fs.readFile(process.argv[2], "utf8", function (error, content) {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
