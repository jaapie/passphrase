import json
import random
import nltk

def clean(l):
  l = list(set(l))
  # random.shuffle(l)
  return l

def good_word(w):
  return w.isalpha() and w[-1:] is not 's'

def get_words(words):
  typed_words = [a[0].lower() for a in words if good_word(a[0])]
  return clean(typed_words)

def get_words_by(words, part):
  typed_words = [a[0].lower() for a in words if a[1] == part and good_word(a[0])]
  return clean(typed_words)

def get_words_of_types(words, types):
  typed_words = [a[0].lower() for a in words if a[1] in types and good_word(a[0])]
  return clean(typed_words)

def main():
  words = nltk.corpus.brown.tagged_words()

  # tags from http://www.comp.leeds.ac.uk/ccalas/tagsets/brown.html
  filtered_words = get_words_of_types(words, ['NN', 'NNS', 'NP', 'NPS',
      'NR', 'NRS', 'PN', 'OD', 'JJ', 'JJR', 'JJS', 'JJT', 'QL', 'RB', 'RBR',
      'RBT', 'RN', 'RT', 'VB', 'VBD', 'VBG', 'VBN', 'VBZ', 'FW-NN'])

  print json.dumps({
      'words': filtered_words
    })

  # print 'there are ' + repr(len(filtered_words)) + ' words in the list'

main()
