'''
Created on 20 Apr 2012

@author: adambednarski
'''

import unittest 
import periscope

class TestSelectBestSubtitle(unittest.TestCase):
    
    def setUp(self):
        self.subtitles = []
        self.subtitlesPl = []
        self.subtitlesEng = []
        self.periscope = periscope.Periscope("/")        
        
    def populateBasicSubtitles(self):
        self.subtitles.append("item1")
        self.subtitles.append("item2")
        self.subtitles.append("item3")        
        
    def populateLanguageSubtitles(self):
        subtitlesPl = []      
        subtitle1Pl["lang"] = "pl"  
        subtitlesPl.append("item1pl")
        subtitlesPl.append("item2pl")
        subtitlesPl.append("item3pl")
        subtitlesEng = []             
        subtitlesEng.append("item1eng")
        subtitlesEng.append("item2eng")
        subtitlesEng.append("item3eng")        
        self.subtitles = {'pl': subtitlesPl, 'eng': subtitlesEng}
        
    def test_selectBestSubtitle_noSubtitles(self):                     
        self.subtitles = []
        result = self.periscope.selectBestSubtitle(self.subtitles)        
        self.assertIsNone(result, "Expecting empty list")
    
    def test_selectBestSubtitle_noLang_noNumber(self):
        self.populateBasicSubtitles()                
        result = self.periscope.selectBestSubtitle(self.subtitles)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
    
    def test_selectBestSubtitle_noLang_number1(self):
        self.populateBasicSubtitles()    
        result = self.periscope.selectBestSubtitle(self.subtitles, number = 1)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))

    def test_selectBestSubtitle_noLang_number2(self):
        self.populateBasicSubtitles()
        result = self.periscope.selectBestSubtitle(self.subtitles, number = 2)        
        self.assertEqual(2, len(result), "Expecting one result only but found %s" % len(result))        

    def test_selectBestSubtitle_lang1_noNumber(self):
        self.populateLanguageSubtitles()
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["pl"], number = 2)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))        
        