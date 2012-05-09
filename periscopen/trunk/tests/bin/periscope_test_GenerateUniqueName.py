'''
Created on 20 Apr 2012

@author: adambednarski
'''

import unittest 
import periscope
from periscope.plugins.OpenSubtitles import OpenSubtitles

class OpenSubtitles():
    pass

class NapisyInfo():
    pass

class MySubtitles():
    pass

class TestGenerateUniqueName(unittest.TestCase):
    
    def setUp(self):
        self.subtitles = []        
        self.periscope = periscope.Periscope("/")
        self.openSubtitlesPlugin = OpenSubtitles()
        self.napisyInfoPlugin = NapisyInfo()
        self.mySubtitlesPlugin = MySubtitles()
        self.periscope.pluginNames = [self.openSubtitlesPlugin.__class__.__name__, self.napisyInfoPlugin.__class__.__name__, self.mySubtitlesPlugin.__class__.__name__]
        self.populateSubtitles() 
            
    def populateSubtitles(self):              
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "1", 
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.OpenSubtitles_en_1.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "2",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.OpenSubtitles_en_2.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "3",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.OpenSubtitles_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "1",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.OpenSubtitles_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "2",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.OpenSubtitles_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "3",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.OpenSubtitles_pl_3.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin,  'index' : "1",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.NapisyInfo_en_1.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "2", 
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.NapisyInfo_en_2.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "3",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.NapisyInfo_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "1",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.NapisyInfo_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "2",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.NapisyInfo_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "3",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.NapisyInfo_pl_3.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "1",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.MySubtitles_en_1.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "2", 
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.MySubtitles_en_2.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "3",
                                'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.MySubtitles_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "1",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.MySubtitles_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "2",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.MySubtitles_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "3",
                               'base_name': "A_MOVIE.srt" ,'indexed_name': "A_MOVIE.MySubtitles_pl_3.srt"})
    
    def test_generateUniqueName(self):
        for subtitle in self.subtitles:
            self.runSingleGenerateUniqueNameTest(subtitle)
            
    def test_generateGenericName(self):
        for subtitle in self.subtitles:
            self.runSingleGenerateGenericNameTest(subtitle)
            
    def runSingleGenerateUniqueNameTest(self, testSubtitle):        
        generatedName = self.periscope.generateUniqueSubtitleName(testSubtitle["index"], testSubtitle)
        expectedName = testSubtitle["indexed_name"]                
        self.assertEqual(generatedName, expectedName, "Incorrect indexed name generated: %s, expected: %s" % (generatedName, expectedName))
    
    def runSingleGenerateGenericNameTest(self, testSubtitle):        
        generatedName = self.periscope.generateBasicSubtitleName(testSubtitle)
        expectedName = testSubtitle["base_name"]                
        self.assertEqual(generatedName, expectedName, "Incorrect base name generated: %s, expected: %s" % (generatedName, expectedName))
        
if __name__ == '__main__':
    unittest.main()  