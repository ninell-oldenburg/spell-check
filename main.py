# -*- coding: utf-8 -*-
# main.py
# Ninell Oldenburg
# Python3
# 04/02/2018
# University of Potsdam


import sys
from include.trie import ReadFile
from include.edit_distance import EditDistance
from include.spell_check import SpellCheck


class Main :
    # init filename of the wordlist and treshold
    def __init__(self,filename,treshold) :
        self.wordlist = ReadFile(filename)
        self.treshold = int(treshold)
        
    # computes corrections
    def compute(self,input_string) :
        if not input_string :
            return None
        # if input string in wordlist > string is valid
        if self.wordlist.trie.validWord(input_string) :
            return 'Input correct'
        # if not > search for another word
        else :
            spellcheck = SpellCheck(self.wordlist.trie,self.treshold)
            result = spellcheck.findOutput(input_string)
            return ' '.join(result)
        
if __name__ == '__main__' :
    # input has to be python file, file nmae and edit distance
    if len(sys.argv) != 3 :
        print('Correct use {0}: main.py wordlist_name edit_distance'.format(sys.argv[0]))
    # no we can change to 'interactice mode'
    else :
        print('loading...')
        function = Main(sys.argv[1],sys.argv[2])
        word = function.compute(input('Type a word: ').strip())
        
        # if input is empty program shuts down
        while not word == None:
            if word == '' :
                print('Cannot find a word with edit distance of {0}'.format(function.treshold))
            elif not word == 'Input correct' :
                print('Did you mean {0}?'.format(word))
            else : print(word)
            word = function.compute(input('Type a word: ').strip())
        print('Program shuts down...')
        
