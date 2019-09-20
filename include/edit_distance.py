# -*- coding: utf-8 -*-
# edit_distance.py
# Ninell Oldenburg
# Python3
# 04/02/2018
# University of Potsdam

import sys

class EditDistance :
    
    # create matrice from length of both strings and make values 0 or None
    def __init__(self,inputString,outputString,treshold) :
        self.input = inputString
        self.output = outputString
        self.matrix = [[j if (i==0) else None for j in range(0,len(self.output)+1)] for i in range(0,len(self.input)+1)]
        self.treshold = treshold
        
    # computation of edit distance by Oflazer (1996)
    def editDistance(self,i,j) :
        # if one string is of length 1, ed is length of the longer one
        if (i==-1 or j==-1) :
            return max(len(self.input),len(self.output))
        # check if ed has already been computed
        if not self.matrix[i][j] == None :
            return self.matrix[i][j]
        # compute recursively to which point the last letters are equal
        if self.input[i-1] == self.output[j-1] :
            self.matrix[i][j] = self.editDistance(i-1,j-1)
            return self.matrix[i][j]
        # ed is 1 if last letters are switched
        if i>1 and j>1 and self.input[i-2] == self.output[j-1] and self.input[i-1] == self.output[j-2] :
            self.matrix[i][j] = 1+min(self.editDistance(i-2,j-2), self.editDistance(i,j-1), self.editDistance(i-1,j))
            return self.matrix[i][j]
        # else: compute ed of the previous letters
        self.matrix[i][j] = 1+min(self.editDistance(i-1,j-1), self.editDistance(i,j-1), self.editDistance(i-1,j))
        return self.matrix[i][j]
    
    # cutoff-ed by Oflazer (1996)
    def cutOffDistance(self) :
        # compute confidence interval of accepted strings
        h = min(len(self.input),len(self.output)+self.treshold)
        l = max(1,len(self.output)-self.treshold)
        result = sys.maxsize
        # compute minimum value of accepted strings
        for i in range(l,h+1) :
            edit = self.editDistance(i,len(self.output))
            result = min(edit,result)
        return result
            
if __name__ == '__main__':
    ed = EditDistance('reprter','repo',2)
    print(ed.cutOffDistance())
        
