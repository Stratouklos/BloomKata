__author__ = 'exak'

from bloom_kata import wordlist

def load():
    var = wordlist.words.split()
    return len(var)