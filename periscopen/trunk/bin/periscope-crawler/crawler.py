#!/usr/bin/python


import os, sys


class Directory():
	def __init__(self, directoryPath):
		self.path = directoryPath
	
	def accept (self, fileVisitor):
		for file in self.fileList:
			fileVisitor.visit(file);
		
	def listFiles(self):		
		self.fileList = os.listdir(self.path)
		for file in self.fileList:
			File(os.path.join(self.path,file.name))


class File():	
	def __init__(self, filePath):
		self.path = filePath
	
	def accept(self, fileVisitor):
		fileVisitor.visit(self)
	
	def getFilePath(self):
		return os.path.realpath(self.path)
		
	def getFileExtension(self):
		extension = self.path.rsplit(".", 1)[1]
		return extension

class Crawler():
	
	def crawl(self, directoryPath, processor):
		directory = Directory(self.directoryPath)
		processor.visit(directory)

	
class SubtitlesDownloaderVisitor():
	def __init__(acceptedExtensions, downloaderApplication):
		self.acceptedExtensions = acceptedExtensions
		self.downloaderApplication = downloaderApplication
	
	def visit(self, file):
		if(file.getFileExtension in self.acceptedExtensions):
			self.downloadSubtitles(file)
	
	def downloadSubtitles(self, file):
		downladerCommand = self.downloaderApplication + " " + file.getFilePath()
		try:		
			os.system(downladerCommand)
		except OSError, (errno, strerror):
			print "Exception occured while downloading subtitles for file: %s, error: %s, message: %s" % (file, errno, strerror)
			
class DeleteVisitor():
	def __init__(acceptedExtensions):
		self.acceptedExtensions = acceptedExtensions
		
	def visit(self, file):
		if(file.getFileExtension in self.acceptedExtensions):
			self.delete(file)
	
	def delete(self, file):
		os.unlink(file.getFilePath)


class SubtitlesConverterVisitor():
	def __init__(acceptedExtensions, coverterApplication):
		self.acceptedExtensions = acceptedExtensions
		self.coverterApplication = coverterApplication
		
	def visit(self, file):
		if(file.getFileExtension in self.acceptedExtensions):
			self.convert(file)
	
	def convert(self, file): 
		inputSubtitle = file.getFilePath()
		outputSubtitle = file.getFilePath() + ".subrip"
		converterCommand = self.coverterApplication + " " + inputSubtitle + " " + outputSubtitle
		try:		
			os.system(converterCommand)
		except OSError, (errno, strerror):
			print "Exception occured while converting file: %s, error: %s, message: %s" % (file,errno,strerror)


class Main():
	
	def workingDirectory(self, workingDirectory):
		self.workingDirectory = workingDirectory
		
	def setDownloaderCommand(self, downloaderCommand):
		self.downloaderCommand = downloaderCommand
		
	def setConverterCommand(self, converterCommand):
		self.converterCommand = converterCommand
		
	def process(self):
		movieCrawler = Crawler()
		downloader = SubtitlesDownloaderVisitor(self.downloaderCommand)
		converter = SubtitlesConverterVisitor(self.converterCommand, ("srt"))				
		remover = DeleteVisitor("srt")
		renamer = RenameVisitor("subrip", "srt")
		movieCrawler = Crawler(self.workingDirectory, downloader)
		movieCrawler = Crawler(self.workingDirectory, converter)
		movieCrawler = Crawler(self.workingDirectory, remover)
		movieCrawler = Crawler(self.workingDirectory, renamer)


if __name__ == "__main__":
	mainProcessor = Main()
	downloader = sys.argv[2] # "/opt/subtitles/periscopen/run.sh"
	mainProcessor.setDownloaderCommand(downloader)
	converter = sys.argv[3] # "/opt/subtitles/sub2srt-0.5.2/run.sh"
	mainProcessor.setConverterCommand(converter);
	mainProcessor.process()
    
	
	TODO : make it work !!!!!
	TODO : make it work !!!!!
	TODO : make it work !!!!!




class FindSubtitles():
	''' loops over directory and subdirectories to find subtitles'''
	
	def __init__(self, workingDirectory = "", movieFileExtensions = ["avi","mkv"], downloader = "", converter = ""):       
		self.workingDirectory = workingDirectory
		self.movieFileExtensions = movieFileExtensions
		self.downloader = downloader
		self.converter = converter
		
	def downloadSubtitles(self, downloader, moviePath, movieFile):
		movie = moviePath + "/" + movieFile
		print "Downloading subtitles for movie %s" % movie 
		downloaderCommand = downloader + " " + movie
		try:		
			os.system(downloaderCommand)
		except OSError, (errno, strerror):
			print "Exception occured while downloading subtitles for movie: %s, error: %s, message: %s" % (file,errno,strerror)

	def convertSubtitles(self, converter, subtitlePath, subtitleFile):
		inputSubtitle = subtitlePath + "/" + subtitleFile
		outputSubtitle = subtitlePath + "/" + subtitleFile + ".subrip"
		converterCommand = converter + " " + inputSubtitle + " " + outputSubtitle
		try:		
			os.system(converterCommand)
		except OSError, (errno, strerror):
			print "Exception occured while converting file: %s, error: %s, message: %s" % (file,errno,strerror)

	def removeFile(self, subtitlePath, subtitleFile):
		subtitle = subtitlePath + "/" + subtitleFile
		try:		
			os.remove(subtitle)
		except OSError, (errno, strerror):
			print "Exception occured while removing file: %s, error: %s, message: %s" % (file,errno,strerror)

	def renameFile(self, subtitlePath, subtitleFile, extension):
		originalSubtitle = subtitlePath + "/" + subtitleFile
		subtitleName = subtitleFile.rsplit(".")[0]
		subtitleExtensionPart1 = subtitleFile.rsplit(".")[1]
		renamedSubtitle = subtitlePath + "/" + subtitleName + "." + subtitleExtensionPart1 + "." + extension
		try:		
			os.rename(originalSubtitle, renamedSubtitle)
		except OSError, (errno, strerror):
			print "Exception occured while removing file: %s, error: %s, message: %s" % (file,errno,strerror)

	def isMovieFile(self, fileName):
		'''check if file passed is movie'''
		fileArray = fileName.split(".")
		fileExtension = fileArray[-1]		
		if fileExtension in self.movieFileExtensions:
			return True
		else:
			return False
	
	def run(self):
		directory = self.workingDirectory
		downloader = self.downloader
		converter = self.converter
		print "Working directory: %s" % directory
		# download subtitles		
		for root, dirs, files in os.walk(directory):
			for file in files:
				if self.isMovieFile(file):
					downloadSubtitles(downloader, directory, file)
	def loopFilterAndRun(filter, processor):
		# convert subtitles
		for root, dirs, files in os.walk(directory):
			for file in files:
				if file.endswith('.srt'):
					convertSubtitles(converter, directory, file)

		# remove unneeded subtitles
		for root, dirs, files in os.walk(directory):
			for file in files:
				if file.endswith('.srt'):
					removeFile(directory, file)

		# rename subtitles
		for root, dirs, files in os.walk(directory):
			for file in files:
				if file.endswith('.subrip'):
					renameFile(directory, file, "srt")

if __name__ == '__main__':
	directory = sys.argv[1]
	movieFileExtensions = ["avi","mkv"]
	downloader = sys.argv[2] # "/opt/subtitles/periscopen/run.sh"
	converter = sys.argv[3] # "/opt/subtitles/sub2srt-0.5.2/run.sh"
	processor = FindSubtitles(directory, movieFileExtensions, downloader, converter)
	processor.run()