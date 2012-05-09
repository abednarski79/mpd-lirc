import unittest
from crawler import FindSubtitles

class MyTestCase(unittest.TestCase):
	
	def setUp(self):
		self.processor = FindSubtitles(movieFileExtensions = ["avi","mkv"])
	
	def testFileAvi(self):					
		self.assertTrue(self.processor.isMovieFile("Picnic At Hanging Rock [Director's Cut].1975.BRRip.XviD.AC3-VLiS.avi"))
	
	def testFileMkv(self):
		self.assertTrue(self.processor.isMovieFile("Chronicle 2012.mkv"))
	
	def testFileTxt(self):
		self.assertFalse(self.processor.isMovieFile("Torrent downloaded from Extratorrent.com.txt"))
		
if __name__ == '__main__':
    unittest.main()