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
    
    
    def populateShortListSubtitles(self):
        self.subtitles.append({'lang': "pl"})
        self.subtitles.append({'lang': "pl"})
        self.subtitles.append({'lang': "pl"})  
        self.subtitles.append({'lang': "en"})
        self.subtitles.append({'lang': "en"})
        self.subtitles.append({'lang': "en"})
    
    def populateLongListSubtitles(self):
        self.subtitles.append({'lang': "pl"})
        self.subtitles.append({'lang': "pl"})
        self.subtitles.append({'lang': "pl"})  
        self.subtitles.append({'lang': "en"})
        self.subtitles.append({'lang': "en"})
        self.subtitles.append({'lang': "en"})       
        
        
    def test_selectBestSubtitle_noSubtitles(self):                     
        self.subtitles = []
        result = self.periscope.selectBestSubtitle(self.subtitles)        
        self.assertIsNone(result, "Expecting empty list")
    
    def test_selectBestSubtitle_langNone_numberNone(self):   
        self.populateLongListSubtitles()                     
        result = self.periscope.selectBestSubtitle(self.subtitles)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
    
    def test_selectBestSubtitle_langNone_number1(self):
        self.populateLongListSubtitles()        
        result = self.periscope.selectBestSubtitle(self.subtitles, number = 1)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))

    def test_selectBestSubtitle_langNone_number2(self):
        self.populateLongListSubtitles()
        result = self.periscope.selectBestSubtitle(self.subtitles, number = 2)        
        self.assertEqual(2, len(result), "Expecting two results only but found %s" % len(result))        

    def test_selectBestSubtitle_langPl_numberNone(self):
        self.populateLongListSubtitles()        
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["pl"])        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result)) 

    def test_selectBestSubtitle_langPl_number1(self):
        self.populateLongListSubtitles()        
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["pl"], number = 1)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
    
    def test_selectBestSubtitle_langPl_number2(self):
        self.populateLongListSubtitles()
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["pl"], number = 2)        
        self.assertEqual(2, len(result), "Expecting two results only but found %s" % len(result))       
        
    def test_selectBestSubtitle_langPlEng_numberNone(self):
        self.populateLongListSubtitles()
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["pl", "en"])        
        self.assertEqual(2, len(result), "Expecting two results only but found %s" % len(result))
    
    def test_selectBestSubtitle_langPlEng_number1(self):
        self.populateLongListSubtitles()
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["pl", "en"], number = 1)        
        self.assertEqual(2, len(result), "Expecting two results only but found %s" % len(result))

    def test_selectBestSubtitle_langPlEng_number2(self):
        self.populateLongListSubtitles()
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["pl", "en"], number = 2)        
        self.assertEqual(4, len(result), "Expecting four results only but found %s" % len(result))                  
        