/** Textual markov chain generator */

class MarkovMachine {
  /** build markov machine; read in text.*/

  constructor(text) {
    let words = text.split(/[ \r\n]+/);
    this.words = words.filter((c) => c !== "");
    this.makeChains();
  }

  /** set markov chains:
   *
   *  for text of "the cat in the hat", chains will be
   *  {"the": ["cat", "hat"], "cat": ["in"], "in": ["the"], "hat": [null]} */

  makeChains() {
    // TODO
    let chain = {};
    this.words.forEach((word) => {
      // find the position of each instance of word
      let positionsOfWord = [];
      let pos = -1;
      while ((pos = this.words.indexOf(word, pos + 1)) != -1) {
        positionsOfWord.push(pos);
      }

      // add word to chain object and map positions to next word
      if (!(`${word}` in chain)) {
        chain[word] = positionsOfWord.map((position) => {
          return this.words[position + 1];
        });
      }
    });

    return chain;
  }

  /** return random text from chains */

  makeText(numWords = 100) {
    // TODO
  }
}

let mm = new MarkovMachine("the cat in the hat");

console.log(mm.makeChains());

module.exports = {MarkovMachine};
