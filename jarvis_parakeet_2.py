# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:50:39 2015

this one uses this code  https://realpython.com/blog/python/lyricize-a-flask-app-to-create-lyrics-using-markov-chains/

pymarkov stuff from here https://github.com/ketaro/markov-cranberries/blob/master/markov.py

@author: fred
"""

import sys
import re
import random
from random import choice

def make_chains(corpus):
    "takes an input text and string and returns dictionay or markov chains"""
    
    chain = {}
    words = corpus.split()
    
    
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        if (pair in chain):
            chain[pair] += [ words[i+2] ]
        else:
            chain[pair] = [ words[i+2] ]
        
    #print "CHAIN: ", chain
#    print "CHAIN type: ", type(chain)
#    print chain.keys()
#    print chain.values()
#    for k, v in chain:
#        print "KEY: ", k, "VALUE: ", v

    return chain
    
def make_text(chains):
    """takes a dict of markov chains and returns random text based of an original text."""
    
    # Start w a word that starts w a capital letter -- I DON'T WANT THIS / actually want this OR starts with @
    
#    start = 'z'
#    while (start[0][0] != start[0][0].upper()):
#        start = random.choice(chains.keys())
    
    # Trying w/o all init cap    
    start = random.choice(chains.keys())
        
    line = list(start)
    #print "line = list(start): ", line
    
    last = line[-1][-1]
    # while len(line < 10):
    while (not line[-1][-1] in ['.', '?']):
        next = chains[tuple(line[-2:])]
        line += [ choice(next) ]
        
    return " ".join(line)

def main():
    args = sys.argv
    filename = 'fakejarvis.txt'    
    f = open(filename, "r")
    
    # I added the below to clean up file a bit    
    process_file = f.read()
    process_file = str(process_file)    
    twitter_username = re.compile(r'@([A-Za-z0-9_]+)')
    cleaned_usernames = re.sub(twitter_username, '', process_file)
    cleaned_RTs = re.sub('RT', '', cleaned_usernames)
    url_link = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')    
    cleaned_links = re.sub(url_link, '', cleaned_RTs)    
    #print cleaned_links

    chain_dict = make_chains(cleaned_links)

    for i in range(4):
        #for i in range(4):
        print "CHAIN: ", make_text(chain_dict)
    print ""

#random_text = make_text('fakejarvis.txt')
#print random_text

main()