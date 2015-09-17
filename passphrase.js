var brownCorpus = require('./corpus-brown.json');

var BROWN_WORD_COUNT = brownCorpus.words.length;

var adjPrime = 379,
    nounPrime = 2027,
    seed = 0,
    current = 0;

module.exports = generate;
module.exports.generate = generate;

function generate(wordCount, minWordLength, joiner) {
    current += 1;
    var words = [];

    for ( i = 0; i < wordCount; i++ ) {
        words.push(brownCorpus.words[ (seed + (current++ * nounPrime)) % BROWN_WORD_COUNT ]);
    }

    return words.join(joiner);
}

// these options are only configurable before
// you call `next` for the first time
module.exports.seed = function (newSeed) {
    return current === 0 && (seed = newSeed, true);
};

module.exports.adjPrime = function (newPrime) {
    return current === 0 && (adjPrime = newPrime, true);
};

module.exports.nounPrime = function (newPrime) {
    return current === 0 && (nounPrime = newPrime, true);
};
