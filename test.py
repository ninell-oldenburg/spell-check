# -*- coding: utf-8 -*-
# test.py
# Ninell Oldenburg
# Python3
# 04/02/2018

import unittest
from include.trie import ReadFile
from include.spell_check import SpellCheck
from include.edit_distance import EditDistance
from main import Main

# file for testing the classes

class ReadFileTest(unittest.TestCase) :
    
    def test_read_file(self) :
        testfile = ReadFile('data/testlist.txt')
        self.assertTrue(testfile.trie.validWord("Gesang"))
        self.assertTrue(testfile.trie.validWord("derjenige"))
        self.assertTrue(testfile.trie.validWord("diejenige"))
        self.assertTrue(testfile.trie.validWord("dasjenige"))
        self.assertTrue(testfile.trie.validWord("der"))
        self.assertTrue(testfile.trie.validWord("die"))
        self.assertTrue(testfile.trie.validWord("das"))
        self.assertTrue(testfile.trie.validWord("ein"))
        self.assertTrue(testfile.trie.validWord("eine"))
        self.assertTrue(testfile.trie.validWord("mehr"))
        self.assertTrue(testfile.trie.validWord("mehrere"))
        self.assertTrue(testfile.trie.validWord("mehre"))
        
class SpellCheckTest(unittest.TestCase) :
    
    def test_spell(self) :
        spellcheck_object = SpellCheck(ReadFile('data/testlist.txt').trie,2)
        self.assertEqual(spellcheck_object.findOutput('dejenige'),['dasjenige','diejenige','derjenige'])
        self.assertEqual(spellcheck_object.findOutput('Gesangg'),['Gesang'])
        self.assertEqual(spellcheck_object.findOutput('Gesanggggg'),[])
        spellcheck_object = SpellCheck(ReadFile('data/testlist.txt').trie,0)
        self.assertEqual(spellcheck_object.findOutput('der'),['der'])
        self.assertEqual(spellcheck_object.findOutput('eine'),['eine'])
        self.assertEqual(spellcheck_object.findOutput('Gesangg'),[])
        spellcheck_object = SpellCheck(ReadFile('data/testlist.txt').trie,5)
        self.assertEqual(spellcheck_object.findOutput('jenige'),['mehr','mehre','mehrere','ein','eine','dasjenige','die','diejenige','der','derjenige','Gesang'])
        self.assertEqual(spellcheck_object.findOutput('Gesang'),['mehr', 'mehre', 'ein', 'eine', 'das', 'der', 'Gesang'])
        self.assertEqual(spellcheck_object.findOutput('Gesanggggggggg'),[])
        
class EditDistanceTest(unittest.TestCase) :
    
    def test_ed_distance(self) :
        ed_dist_object = EditDistance('re','repo',2)
        self.assertEqual(ed_dist_object.cutOffDistance(),2)
        ed_dist_object = EditDistance('reprte','repo',2)
        self.assertEqual(ed_dist_object.cutOffDistance(),1)
        ed_dist_object = EditDistance('repo','repo',0)
        self.assertEqual(ed_dist_object.cutOffDistance(),0)
        ed_dist_object = EditDistance('rprt','repo',2)
        self.assertEqual(ed_dist_object.cutOffDistance(),2)
        ed_dist_object = EditDistance('hello','rapos',2)
        self.assertEqual(ed_dist_object.cutOffDistance(),5)
        
class ApplicationTest(unittest.TestCase) :
    
    def test_application(self) :
        print("tests running...")
        
        main = Main('data/testlist.txt',2)
        self.assertEqual(main.compute('dejenige'),'dasjenige diejenige derjenige')
        self.assertEqual(main.compute('Gesanggg'),'Gesang')
        self.assertEqual(main.compute('Gesanggggg'),'')
        self.assertEqual(main.compute(None),None)
        
        main = Main('data/derewo.txt',2)
        self.assertEqual(main.compute('kein'),'Input correct')
        self.assertEqual(main.compute('keiness'),'keine keiner keines eines')
        self.assertEqual(main.compute('keinessss'),'')
        self.assertEqual(main.compute('der'),'Input correct')
        self.assertEqual(main.compute('derselbe'),'Input correct')
        self.assertEqual(main.compute('deselbe'),'Geselle dasselbe dieselbe derselbe')
        self.assertEqual(main.compute('dieseselbe'),'dieselbe')
        self.assertEqual(main.compute('diesenselbe'),'')
        self.assertEqual(main.compute('Fooerderung'),'Forderung')
        self.assertEqual(main.compute(None),None)
                         
        main = Main('data/wordsEn.txt',2)
        self.assertEqual(main.compute('nothing'),'Input correct')
        self.assertEqual(main.compute('nottingham'),'')
        self.assertEqual(main.compute('ridinggg'),'riding ridings')
        self.assertEqual(main.compute(None),None)
        
if __name__ == '__main__' :
    unittest.main()
        
    
