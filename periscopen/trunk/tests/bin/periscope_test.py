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
        self.populateSubtitles()
            
    def populateSubtitles(self):        
        self.subtitles.append({'lang': "en", 'plugin': "opensubtitles", 
                               'test_id': "A_MOVIE.opensubtitles_en_1.srt"})
        self.subtitles.append({'lang': "en", 
                               'test_id': "A_MOVIE.opensubtitles_en_2.srt"})
        self.subtitles.append({'lang': "en", 'plugin': "opensubtitles", 
                               'test_id': "A_MOVIE.opensubtitles_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "opensubtitles",
                               'test_id': "A_MOVIE.opensubtitles_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "opensubtitles",
                               'test_id': "A_MOVIE.opensubtitles_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "opensubtitles",
                               'test_id': "A_MOVIE.opensubtitles_pl_3.srt"})
        self.subtitles.append({'lang': "en", 'plugin': "napisyinfo",
                               'test_id': "A_MOVIE.napisyinfo_en_1.srt"})
        self.subtitles.append({'lang': "en", 'plugin': "napisyinfo", 
                               'test_id': "A_MOVIE.napisyinfo_en_2.srt"})
        self.subtitles.append({'lang': "en", 'plugin': "napisyinfo",
                               'test_id': "A_MOVIE.napisyinfo_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "napisyinfo",
                               'test_id': "A_MOVIE.napisyinfo_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "napisyinfo",
                               'test_id': "A_MOVIE.napisyinfo_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "napisyinfo",
                               'test_id': "A_MOVIE.napisyinfo_pl_3.srt"})
        self.subtitles.append({'lang': "en", 'plugin': "mysubtitles",
                               'test_id': "A_MOVIE.mysubtitles_en_1.srt"})
        self.subtitles.append({'lang': "en", 'plugin': "mysubtitles", 
                               'test_id': "A_MOVIE.mysubtitles_en_2.srt"})
        self.subtitles.append({'lang': "en", 'plugin': "mysubtitles",
                                'test_id': "A_MOVIE.mysubtitles_en_3.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "mysubtitles",
                               'test_id': "A_MOVIE.mysubtitles_pl_1.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "mysubtitles",
                               'test_id': "A_MOVIE.mysubtitles_pl_2.srt"})
        self.subtitles.append({'lang': "pl", 'plugin': "mysubtitles",
                               'test_id': "A_MOVIE.mysubtitles_pl_3.srt"})
    
    
    '''0) special cases'''
        
    '''no subtitles found'''
    def test_selectBestSubtitle_noSubtitles(self):                     
        self.subtitles = []
        result = self.periscope.selectBestSubtitle(self.subtitles)        
        self.assertIsNone(result, "Expecting empty list")


    '''I) mt/mp present or default, language not set or default:'''
        
    '''
    1) mt / mp not set, lang set to "en" (or not set) results in ["Total index number"]:
    A_MOVIE.srt
    this is the default behaviour which is compatibile with most of players, source for these subtitles is A_MOVIE.opensubtitles_en_1.srt
    '''
    def test_selectBestSubtitle_langNone_totalNumberNone(self):
        result = self.periscope.selectBestSubtitle(self.subtitles)  
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt"], self.getTestIds(result), 
                             "Lists do not match");        
    def test_selectBestSubtitle_langEn_totalNumberNone(self):              
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en"])        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result)) 
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt"], self.getTestIds(result), 
                             "Lists do not match");
    '''
    2) mt set to 1, lang set to "en" (or not set) results in ["Total index number"]: results in same result as (1) ["Total index number"]
    '''
    def test_selectBestSubtitle_langEn_totalNumber1(self):  
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en"], totalNumber = 1)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt"], self.getTestIds(result), 
                             "Lists do not match");
                             
    def test_selectBestSubtitle_langNone_totalNumber1(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, totalNumber = 1)        
        self.assertEqual(1, len(result), "Expecting one result only but found %s" % len(result))
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt"], self.getTestIds(result), 
                             "Lists do not match");
                                         
    '''
    3) mt set to 2, lang set to "en" (or not set), results in ["Total index number"]:
    note: additionally first subtitle - A_MOVIE.opensubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    A_MOVIE.srt
    A_MOVIE.opensubtitles_en_1.srt
    A_MOVIE.opensubtitles_en_2.srt
    '''
    def test_selectBestSubtitle_langEn_number2(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en"], totalNumber = 2)        
        self.assertEqual(2, len(result), "Expecting two results but found %s" % len(result))
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt", "A_MOVIE.opensubtitles_en_2.srt"], self.getTestIds(result), 
                             "Lists do not match");
    def test_selectBestSubtitle_langNone_number2(self):       
        result = self.periscope.selectBestSubtitle(self.subtitles, totalNumber = 2)        
        self.assertEqual(2, len(result), "Expecting two results only but found %s" % len(result))      
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt", "A_MOVIE.opensubtitles_en_2.srt"], self.getTestIds(result), 
                             "Lists do not match");
                        
    '''
    TODO
    4) mp set to 1, lang set to "en" (or not set), results in ["Plugin index number"]:
    note: additionally first subtitle - A_MOVIE.opensubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    A_MOVIE.srt
    A_MOVIE.opensubtitles_en_1.srt
    A_MOVIE.napisyinfo_en_1.srt
    A_MOVIE.mysubtitles_en_1.srt
    '''
    
    
    ''''
    TODO
    5) mp set to 2, lang set to "en" (or not set), results in ["Plugin index number"]:
    note: additionally first subtitle - A_MOVIE.opensubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    A_MOVIE.srt
    A_MOVIE.opensubtitles_en_1.srt
    A_MOVIE.opensubtitles_en_2.srt
    A_MOVIE.napisyinfo_en_1.srt
    A_MOVIE.napisyinfo_en_2.srt
    A_MOVIE.mysubtitles_en_1.srt
    A_MOVIE.mysubtitles_en_2.srt
    '''
        
    
    '''II) multi languages set, mt/mp not sets or default'''
    
    '''6) mt / mp not set, lang set to "en" and "pl" results in ["Total/language index number"]:
    A_MOVIE.srt
    A_MOVIE.opensubtitles_en_1.srt
    A_MOVIE.opensubtitles_pl_1.srt
    additionally first subtitle - A_MOVIE.opensubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    '''
    def test_selectBestSubtitle_langPlEng_totalNumberNone(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en", "pl"])        
        self.assertEqual(2, len(result), "Expecting two results only but found %s" % len(result))
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt", "A_MOVIE.opensubtitles_pl_1.srt"], self.getTestIds(result), 
                            "Lists do not match");
                              
    '''7) mt set to 1, lang set to "en" and "pl" - same result as (6) ["Total/language index number"]'''
    def test_selectBestSubtitle_langPlEng_totalNumber1(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en", "pl"], totalNumber = 1)        
        self.assertEqual(2, len(result), "Expecting two results but found %s" % len(result))
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt", "A_MOVIE.opensubtitles_pl_1.srt"], self.getTestIds(result), 
                            "Lists do not match");        
        
    '''III) multi languages set, mt/mp set'''
    
    '''8) mt set to 2, lang set to "en" and "pl"
    A_MOVIE.opensubtitles_en_1.srt
    A_MOVIE.opensubtitles_en_2.srt
    A_MOVIE.opensubtitles_pl_1.srt
    A_MOVIE.opensubtitles_pl_2.srt
    additionally first subtitle - A_MOVIE.opensubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    '''
    def test_selectBestSubtitle_langPlEng_number2(self):
        result = self.periscope.selectBestSubtitle(self.subtitles, langs = ["en", "pl"], totalNumber = 2)        
        self.assertEqual(4, len(result), "Expecting four results only but found %s" % len(result))
        self.assertListEqual(["A_MOVIE.opensubtitles_en_1.srt", "A_MOVIE.opensubtitles_en_2.srt", 
                              "A_MOVIE.opensubtitles_pl_1.srt", "A_MOVIE.opensubtitles_pl_2.srt"], self.getTestIds(result), 
                            "Lists do not match");          
                      
    '''
    TODO
    9) mp set to 1, lang set to "en" and "pl"
    A_MOVIE.opensubtitles_en_1.srt
    A_MOVIE.opensubtitles_pl_1.srt
    A_MOVIE.napisyinfo_en_1.srt
    A_MOVIE.napisyinfo_pl_1.srt
    A_MOVIE.mysubtitles_en_1.srt
    A_MOVIE.mysubtitles_pl_1.srt
    additionally first subtitle - A_MOVIE.opensubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    '''

    '''
    TODO
    10) mp set to 2, lang set to "en" and "pl"
    A_MOVIE.opensubtitles_en_1.srt
    A_MOVIE.opensubtitles_en_2.srt
    A_MOVIE.opensubtitles_pl_1.srt
    A_MOVIE.opensubtitles_pl_2.srt
    A_MOVIE.napisyinfo_en_1.srt
    A_MOVIE.napisyinfo_en_2.srt
    A_MOVIE.napisyinfo_pl_1.srt
    A_MOVIE.napisyinfo_pl_2.srt
    A_MOVIE.mysubtitles_en_1.srt
    A_MOVIE.mysubtitles_en_2.srt
    A_MOVIE.mysubtitles_pl_1.srt
    A_MOVIE.mysubtitles_pl_2.srt
    additionally first subtitle - A_MOVIE.opensubtitles_en_1.srt is being save as A_MOVIE.srt for back compatibility
    '''

    def getTestIds(self, list):
        outputList = []
        for item in list:
            outputList.append(item["test_id"])
        return outputList
    
if __name__ == '__main__':
    unittest.main()    