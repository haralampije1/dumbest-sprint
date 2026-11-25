#!/usr/bin/env node
// The Dumbest Thing Your Agent Did Today - Entry
// Writes one line to /output/entry.txt

const fs = require('fs');
const path = require('path');

// The entry line - a concrete, believable agent failure with a punchline
const entry = "My agent spent 47 minutes debugging a typo in a comment, then committed 'fixed typo' with the typo still in it";

const outputDir = '/output';
const outputFile = path.join(outputDir, 'entry.txt');

// Ensure output directory exists
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// Write the entry
fs.writeFileSync(outputFile, entry, 'utf8');
console.log('Entry written:', entry);
console.log('Length:', entry.length, 'chars');