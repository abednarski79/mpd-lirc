'''
Created on 20 Apr 2012

@author: adambednarski
'''

import unittest 
import periscope

class OpenSubtitles():
    pass

class NapisyInfo():
    pass

class MySubtitles():
    pass

class TestSelectBestSubtitle(unittest.TestCase):
    
    def setUp(self):
        self.subtitles = []
        self.subtitlesPl = []
        self.subtitlesEng = []
        self.periscope = periscope.Periscope("/")
        self.openSubtitlesPlugin = OpenSubtitles()
        self.napisyInfoPlugin = NapisyInfo()
        self.mySubtitlesPlugin = MySubtitles()
        self.periscope.pluginNames = [self.openSubtitlesPlugin.__class__.__name__, self.napisyInfoPlugin.__class__.__name__, self.mySubtitlesPlugin.__class__.__name__]        
        self.populateSubtitles()
            
    def populateSubtitles(self):        
        self.subtitles.append({'lang': "en", 'plugin': self.openSubtitlesPlugin, 
                               'test_id': "A_MOVIE.OpenSubtitles_en_1.srt"})
        self.subtitles.append({'lang': "en", 'plugin': self.openSubtitlesPlugin,
                               'test_id': "A_MOVIE.OpenSubtitles_en_2.srt"})
        self.subtitles.append({'lang': "en", 'plugin': self.openSubtitlesPlugin, 
                               'test_id': "A_MOVIE.OpenSubtitles_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.openSubtitlesPlugin,
                               'test_id': "A_MOVIE.OpenSubtitles_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.openSubtitlesPlugin,
                               'test_id': "A_MOVIE.OpenSubtitles_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.openSubtitlesPlugin,
                               'test_id': "A_MOVIE.OpenSubtitles_pl_3.srt"})
        self.subtitles.append({'lang': "en", 'plugin': self.napisyInfoPlugin,
                               'test_id': "A_MOVIE.NapisyInfo_en_1.srt"})
        self.subtitles.append({'lang': "en", 'plugin': self.napisyInfoPlugin, 
                               'test_id': "A_MOVIE.NapisyInfo_en_2.srt"})
        self.subtitles.append({'lang': "en", 'plugin': self.napisyInfoPlugin,
                               'test_id': "A_MOVIE.NapisyInfo_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.napisyInfoPlugin,
                               'test_id': "A_MOVIE.NapisyInfo_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.napisyInfoPlugin,
                               'test_id': "A_MOVIE.NapisyInfo_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.napisyInfoPlugin,
                               'test_id': "A_MOVIE.NapisyInfo_pl_3.srt"})
        self.subtitles.append({'lang': "en", 'plugin': self.mySubtitlesPlugin,
                               'test_id': "A_MOVIE.MySubtitles_en_1.srt"})
        self.subtitles.append({'lang': "en", 'plugin': self.mySubtitlesPlugin, 
                               'test_id': "A_MOVIE.MySubtitles_en_2.srt"})
        self.subtitles.append({'lang': "en", 'plugin': self.mySubtitlesPlugin,
                                'test_id': "A_MOVIE.MySubtitles_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.mySubtitlesPlugin,
                               'test_id': "A_MOVIE.MySubtitles_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.mySubtitlesPlugin,
                               'test_id': "A_MOVIE.MySubtitles_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': self.mySubtitlesPlugin,
                               'test_id': "A_MOVIE.MySubtitles_pl_3.srt"})
    
    
    '''0) special cases'''
        
    '''no subtitles found'''
    def test_selectBestSubtitle_noSubtitles(self):                     
        self.subtitles = []
        result = self.periscope.selectBestSubtitle(self.subtitles)        
        self.assertTrue(result == None, "Expecting empty list")


    '''I) mt/mp present or default, language not set or default:'''
        
    '''
    1) mt / mp not set, lang set to "en" (or not set) results in ["Total index number"]:
    A_MOVIE.srt
    this is the default behaviour which is compatibile with most of players, source for these subtitles is A_MOVIE.OpenSubtitles_en_1.srt
    '''
    def test_selectBestSubtitle_langNone_maxTotalNumberNone(self):
        result = self.periscope.selectBestSubtitle(self.subtitles)  
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt"], self.getTestIds(result), 
                             "Lists do not match");        
    def test_selectBestSubtitle_langEn_maxTotalNumberNone(self):              
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en"])        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result)) 
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt"], self.getTestIds(result), 
                             "Lists do not match");
    '''
    2) mt set to 1, lang set to "en" (or not set) results in ["Total index number"]: results in same result as (1) ["Total index number"]
    '''
    def test_selectBestSubtitle_langEn_maxTotalNumber1(self):  
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en"], maxTotalNumber = 1)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt"], self.getTestIds(result), 
                             "Lists do not match");
                             
    def test_selectBestSubtitle_langNone_maxTotalNumber1(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, maxTotalNumber = 1)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt"], self.getTestIds(result), 
                             "Lists do not match");
                                         
    '''
    3) mt set to 2, lang set to "en" (or not set), results in ["Total index number"]:
    note: additionally first subtitle - A_MOVIE.OpenSubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    A_MOVIE.srt
    A_MOVIE.OpenSubtitles_en_1.srt
    A_MOVIE.OpenSubtitles_en_2.srt
    '''
    def test_selectBestSubtitle_langEn_maxTotalNumber2(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en"], maxTotalNumber = 2)        
        self.assertEqual(2, len(result), "Expecting two results but found %s" % len(result))
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt", "A_MOVIE.OpenSubtitles_en_2.srt"], self.getTestIds(result), 
                             "Lists do not match");
    def test_selectBestSubtitle_langNone_maxTotalNumber2(self):       
        result = self.periscope.selectBestSubtitle(self.subtitles, maxTotalNumber = 2)        
        self.assertEqual(2, len(result), "Expecting two results only but found %s" % len(result))              
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt", "A_MOVIE.OpenSubtitles_en_2.srt"], self.getTestIds(result), 
                             "Lists do not match");
                        
    '''
    4) mp set to 1, lang set to "en" (or not set), results in ["Plugin index number"]:
    note: additionally first subtitle - A_MOVIE.OpenSubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    A_MOVIE.srt
    A_MOVIE.OpenSubtitles_en_1.srt
    A_MOVIE.NapisyInfo_en_1.srt
    A_MOVIE.MySubtitles_en_1.srt
    '''
    def test_selectBestSubtitle_langNone_maxNumberPerPlugin1(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, maxNumberPerPlugin = 1)
        self.assertEqual(3, len(result), "Expecting three results only but found %s" % len(result))
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt", "A_MOVIE.NapisyInfo_en_1.srt", "A_MOVIE.MySubtitles_en_1.srt"], 
                             self.getTestIds(result), "Lists do not match");        
        
    ''''
    5) mp set to 2, lang set to "en" (or not set), results in ["Plugin index number"]:
    note: additionally first subtitle - A_MOVIE.OpenSubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    A_MOVIE.srt
    A_MOVIE.OpenSubtitles_en_1.srt
    A_MOVIE.OpenSubtitles_en_2.srt
    A_MOVIE.NapisyInfo_en_1.srt
    A_MOVIE.NapisyInfo_en_2.srt
    A_MOVIE.MySubtitles_en_1.srt
    A_MOVIE.MySubtitles_en_2.srt
    '''
    def test_selectBestSubtitle_langNone_maxNumberPerPlugin2(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, maxNumberPerPlugin = 2)
        self.assertEqual(6, len(result), "Expecting six results only but found %s" % len(result))        
        self.assertEqual([
            "A_MOVIE.OpenSubtitles_en_1.srt",
            "A_MOVIE.OpenSubtitles_en_2.srt",
            "A_MOVIE.NapisyInfo_en_1.srt",
            "A_MOVIE.NapisyInfo_en_2.srt",
            "A_MOVIE.MySubtitles_en_1.srt",
            "A_MOVIE.MySubtitles_en_2.srt"], 
            self.getTestIds(result), "Lists do not match");        
        
    
    '''II) multi languages set, mt/mp not sets or default'''
    
    '''6) mt / mp not set, lang set to "en" and "pl" results in ["Total/language index number"]:
    A_MOVIE.srt
    A_MOVIE.OpenSubtitles_en_1.srt
    A_MOVIE.OpenSubtitles_pl_1.srt
    additionally first subtitle - A_MOVIE.OpenSubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    '''
    def test_selectBestSubtitle_langPlEng_maxTotalNumberNone(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en", "pl"])        
        self.assertEqual(2, len(result), "Expecting two results only but found %s" % len(result))
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt", "A_MOVIE.OpenSubtitles_pl_1.srt"], self.getTestIds(result), 
                            "Lists do not match");
                              
    '''7) mt set to 1, lang set to "en" and "pl" - same result as (6) ["Total/language index number"]'''
    def test_selectBestSubtitle_langPlEng_maxTotalNumber1(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en", "pl"], maxTotalNumber = 1)        
        self.assertEqual(2, len(result), "Expecting two results but found %s" % len(result))
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt", "A_MOVIE.OpenSubtitles_pl_1.srt"], self.getTestIds(result), 
                            "Lists do not match");        
        
    '''III) multi languages set, mt/mp set'''
    
    '''8) mt set to 2, lang set to "en" and "pl"
    A_MOVIE.OpenSubtitles_en_1.srt
    A_MOVIE.OpenSubtitles_en_2.srt
    A_MOVIE.OpenSubtitles_pl_1.srt
    A_MOVIE.OpenSubtitles_pl_2.srt
    additionally first subtitle - A_MOVIE.OpenSubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    '''
    def test_selectBestSubtitle_langPlEng_maxTotalNumber2(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en", "pl"], maxTotalNumber = 2)        
        self.assertEqual(4, len(result), "Expecting four results only but found %s" % len(result))
        self.assertEqual(["A_MOVIE.OpenSubtitles_en_1.srt", "A_MOVIE.OpenSubtitles_en_2.srt", 
                              "A_MOVIE.OpenSubtitles_pl_1.srt", "A_MOVIE.OpenSubtitles_pl_2.srt"], self.getTestIds(result), 
                            "Lists do not match");          
                      
    '''    
    9) mp set to 1, lang set to "en" and "pl"
    A_MOVIE.OpenSubtitles_en_1.srt
    A_MOVIE.MySubtitles_en_1.srt
    A_MOVIE.NapisyInfo_en_1.srt
    A_MOVIE.OpenSubtitles_pl_1.srt
    A_MOVIE.NapisyInfo_pl_1.srt    
    A_MOVIE.MySubtitles_pl_1.srt
    additionally first subtitle - A_MOVIE.OpenSubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    '''
    
    def test_selectBestSubtitle_langPlEng_maxNumberPerPlugin1(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en", "pl"], maxNumberPerPlugin = 1)        
        self.assertEqual(6, len(result), "Expecting six results only but found %s" % len(result))
        self.assertEqual([
            "A_MOVIE.OpenSubtitles_en_1.srt",            
            "A_MOVIE.NapisyInfo_en_1.srt",
            "A_MOVIE.MySubtitles_en_1.srt",
            "A_MOVIE.OpenSubtitles_pl_1.srt",
            "A_MOVIE.NapisyInfo_pl_1.srt",            
            "A_MOVIE.MySubtitles_pl_1.srt"], 
            self.getTestIds(result), "Lists do not match");
    '''
    10) mp set to 2, lang set to "en" and "pl"
    A_MOVIE.OpenSubtitles_en_1.srt
    A_MOVIE.OpenSubtitles_en_2.srt
    A_MOVIE.NapisyInfo_en_1.srt
    A_MOVIE.NapisyInfo_en_2.srt
    A_MOVIE.MySubtitles_en_1.srt
    A_MOVIE.MySubtitles_en_2.srt
    A_MOVIE.OpenSubtitles_pl_1.srt
    A_MOVIE.OpenSubtitles_pl_2.srt    
    A_MOVIE.NapisyInfo_pl_1.srt
    A_MOVIE.NapisyInfo_pl_2.srt    
    A_MOVIE.MySubtitles_pl_1.srt
    A_MOVIE.MySubtitles_pl_2.srt
    additionally first subtitle - A_MOVIE.OpenSubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    '''
    def test_selectBestSubtitle_langPlEng_maxNumberPerPlugin2(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en", "pl"], maxNumberPerPlugin = 2)        
        self.assertEqual(12, len(result), "Expecting twelve results only but found %s" % len(result))
        self.assertEqual([
            "A_MOVIE.OpenSubtitles_en_1.srt",
            "A_MOVIE.OpenSubtitles_en_2.srt",
            "A_MOVIE.NapisyInfo_en_1.srt",
            "A_MOVIE.NapisyInfo_en_2.srt",
            "A_MOVIE.MySubtitles_en_1.srt",
            "A_MOVIE.MySubtitles_en_2.srt",
            "A_MOVIE.OpenSubtitles_pl_1.srt",
            "A_MOVIE.OpenSubtitles_pl_2.srt",  
            "A_MOVIE.NapisyInfo_pl_1.srt",
            "A_MOVIE.NapisyInfo_pl_2.srt",    
            "A_MOVIE.MySubtitles_pl_1.srt",
            "A_MOVIE.MySubtitles_pl_2.srt"], 
            self.getTestIds(result), "Lists do not match");
            
    def getTestIds(self, list):
        outputList = []
        for item in list:
            outputList.append(item["test_id"])
        return outputList
    
if __name__ == '__main__':
    unittest.main()    