# -*- coding: utf-8 -*-
# spell_check.py
# Ninell Oldenburg
# Python3
# 04/02/2018
# University of Potsdam

from include.edit_distance import EditDistance


# class to find correct word with given edit distance (ed)
class SpellCheck :
    # contructor with trie and treshold
    def __init__(self,trie,treshold) :
        self.trie = trie
        self.treshold = treshold
        
    def findOutput(self,inputString) :
        # accroding to Olfazer (1996):
        result = []
        stack = []
        stack.append(self.trie.root)
        
        while stack :
            currentNode = stack.pop()
            # children is a dict
            for char,node in currentNode.children.items() :
                edit_dist = EditDistance(inputString,node.label,self.treshold)
                if edit_dist.cutOffDistance() <= self.treshold :
                    stack.append(node)
                # if ed of input and child is valid and word is valid append word to result list
                if edit_dist.editDistance(len(inputString),len(node.label)) <= self.treshold and node.isWord :
                    result.append(node.label)
                        
        return result
