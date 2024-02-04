#!/usr/bin/node
const fs = require("fs");

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  console.error("Usage: node 1-writeme.js <file_path> <content_to_write>");
  process.exit(1);
}

fs.writeFile(filePath, contentToWrite, "utf8", (error) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`Content written to ${filePath}`);
  }
});
