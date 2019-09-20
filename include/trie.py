# -*- coding: utf-8 -*-
# trie.py
# Ninell Oldenburg
# Python3
# 04/02/2018
# University of Potsdam


import sys

class Node:
    # children is dict; isword is bool for end of the word
    def __init__(self,label) :
        self.label = label
        self.children = dict()
        self.isWord = False
        
    def addChild(self,letter) :
        if not letter in self.children.keys() :
            # every child has current word + current letter as value
            self.children[letter] = Node(self.label+letter)
        # returning the node now is easier for the addWord function
        return self.children[letter]
    
class Trie :
    def __init__(self) :
        self.root = Node('')
     
    def addWord(self,word) :
        currentNode = self.root
        for letter in word :
            currentNode = currentNode.addChild(letter)
        # last node marks end of the word
        currentNode.isWord = True

    # check if a given word is in the trie (and valid)
    def validWord(self,word) :
        currentNode = self.root
        for letter in word :
            if letter in currentNode.children.keys() :
                currentNode = currentNode.children[letter]
            else :
                return False
        return currentNode.isWord
    
# reading a word list
class ReadFile :
    def __init__(self,wordlist) :
        # coding is in line with the word list of IDS Mannheim
        self.trie = Trie()
        self.wordlist = open(wordlist,'r',encoding='ISO-8859-15')
        # every word is one word in trie
        for line in self.wordlist.readlines() :
            if not line[0] == '#' :
                for word in self.cut_words(line) :
                    self.trie.addWord(word)
        # don't forget to close file!
        self.wordlist.close( )
            
    # cutting words properly
    def cut_words(self,word) :
        word = word[:word.find(' ')]
        result = []
        # compute every form of a lemma
        if '(' in word :
            lemma = word[:word.find('(')]
            suffix = word[word.find('(')+1:word.find(')')].split(',')
            for pos in range(0,len(suffix)) :
                result.append(lemma+suffix[pos])
            result.append(lemma)
    
        elif '/' in word :
            wordlist = word.split('/')
            length = len(wordlist[0])
            suffix = wordlist[len(wordlist)-1][length:]
            for pos in range(0,len(wordlist)-1) :
                result.append(wordlist[pos]+suffix)
            result.append(wordlist[len(wordlist)-1])
    
        elif ',' in word :
            wordlist = word.split(',')
            for char in wordlist :
                result.append(char)
        
        else :
            result.append(word)

        return result
    
if __name__ == '__main__':
    trie = ReadFile(sys.argv[1])
    print(trie.trie.validWord('auch'))
    print(trie.trie.validWord('hg.ichT'))
    print(trie.trie.validWord('auf'))
    print(trie.trie.validWord('Mein'))
    print(trie.trie.validWord('es'))
        
      
