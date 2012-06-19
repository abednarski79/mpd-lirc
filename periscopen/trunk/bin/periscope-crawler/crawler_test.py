import unittest
from crawler import SubtitlesConverterVisitor

class MyTestCase(unittest.TestCase):
	
	def setUp(self):
		metaInfoReaderResultMap = {'/mnt/nasfiles/Torrent/The_Kings_Speech_2010/The_Kings_Speech_2010.avi': '23.976'}		
		self.converter = SubtitlesConverterVisitor(("srt"), "some bash command", metaInfoReaderResultMap)		
	
	def test_converter_findMatchingFile(self):		
		subtitle1 = "/mnt/nasfiles/Torrent/The_Kings_Speech_2010/The_Kings_Speech_2010.OpenSubtitles_pl_1.srt"
		subtitle2 = "/mnt/nasfiles/Torrent/The_Kings_Speech_2010/The_Kings_Speech_2010.OpenSubtitles_en_3.srt"
		result = self.converter.findMatchingFile(subtitle1)
		expected = "23.976"
		self.assertTrue(result == expected, "Can't find matching information");		
	
if __name__ == '__main__':
    unittest.main()