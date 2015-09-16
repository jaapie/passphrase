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

def main():
  words = nltk.corpus.brown.tagged_words()

  print json.dumps({
      'words': get_words(words)
    })

  # print 'there are ' + repr(len(words)) + ' words in the list'

main()
