#!/usr/bin/env node

var package = require("./package.json");
var program = require("commander");
var passphrase = require("./passphrase.js");
var corpus = require("./corpus-brown.json");

program
    .version(package.version)
    .option('-w, --word-count <count>', 'number of words in passphrase', 3)
    .option('-l, --min-length <length>', 'minimum length for each word', 4)
    .option('-s, --separator <char>', 'character used for word separator', ' ')
    .parse(process.argv);

with (Math) {
    passphrase.seed(floor(random() * corpus.words.length));

    console.log(passphrase.generate(program.wordCount, program.minLength,
                program.separator));
}
