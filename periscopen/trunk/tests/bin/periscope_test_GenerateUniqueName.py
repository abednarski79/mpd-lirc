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
                               'expected_name': "A_MOVIE.OpenSubtitles_en_1.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "2",
                               'expected_name': "A_MOVIE.OpenSubtitles_en_2.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "3",
                               'expected_name': "A_MOVIE.OpenSubtitles_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "1",
                               'expected_name': "A_MOVIE.OpenSubtitles_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "2",
                               'expected_name': "A_MOVIE.OpenSubtitles_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.openSubtitlesPlugin, 'index' : "3",
                               'expected_name': "A_MOVIE.OpenSubtitles_pl_3.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin,  'index' : "1",
                               'expected_name': "A_MOVIE.NapisyInfo_en_1.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "2", 
                               'expected_name': "A_MOVIE.NapisyInfo_en_2.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "3",
                               'expected_name': "A_MOVIE.NapisyInfo_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "1",
                               'expected_name': "A_MOVIE.NapisyInfo_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "2",
                               'expected_name': "A_MOVIE.NapisyInfo_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.napisyInfoPlugin, 'index' : "3",
                               'expected_name': "A_MOVIE.NapisyInfo_pl_3.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "1",
                               'expected_name': "A_MOVIE.MySubtitles_en_1.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "2", 
                               'expected_name': "A_MOVIE.MySubtitles_en_2.srt"})
        self.subtitles.append({'lang': "en", 'filename': "A_MOVIE.avi",'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "3",
                                'expected_name': "A_MOVIE.MySubtitles_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "1",
                               'expected_name': "A_MOVIE.MySubtitles_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "2",
                               'expected_name': "A_MOVIE.MySubtitles_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'filename': "A_MOVIE.avi",'plugin': self.mySubtitlesPlugin, 'index' : "3",
                               'expected_name': "A_MOVIE.MySubtitles_pl_3.srt"})
    
    def test_generateUniqueName(self):
        for subtitle in self.subtitles:
            self.runSingleTest(subtitle)
            
    def runSingleTest(self, testSubtitle):        
        generatedName = self.periscope.generateUniqueSubtitleName(testSubtitle["index"], testSubtitle)
        expectedName = testSubtitle["expected_name"]                
        self.assertEqual(generatedName, expectedName, "Incorrect name generted: %s, expected: %s" % (generatedName, expectedName))
    
if __name__ == '__main__':
    unittest.main()  