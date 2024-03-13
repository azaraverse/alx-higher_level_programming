#!/usr/bin/node

const fs = require('fs');

// get file paths from commandline
const sourceFileA = process.argv[2];
const sourceFileB = process.argv[3];
const destionationFile = process.argv[4];

// read content from files
const contentA = fs.readFileSync(sourceFileA, 'UTF-8');
const contentB = fs.readFileSync(sourceFileB, 'UTF-8');

// concat content from both files
const concatContent = contentA + contentB;

// write concatenated content to destination file
fs.writeFileSync(destionationFile, concatContent);
