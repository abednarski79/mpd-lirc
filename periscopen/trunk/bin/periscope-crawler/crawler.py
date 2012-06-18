#!/usr/bin/python


import os, sys
import logging
import subprocess
import shutil
from optparse import OptionParser

class Directory():
	def __init__(self, directoryPath):		
		self.path = directoryPath
		self.listFiles()
	
	def accept (self, fileVisitor):
		for file in self.fileList:
			fileVisitor.visit(file);
		
	def listFiles(self):
		self.fileList = []
		for root, dirs, files in os.walk(self.path):			
			for file in files:
				self.fileList.append(File(os.path.join(root, file)))

class File():	
	def __init__(self, filePath):
		self.path = filePath
	
	def accept(self, fileVisitor):
		fileVisitor.visit(self)
	
	def getFilePath(self):
		return self.path
		
	def getFileExtension(self):
		extension = self.path.rsplit(".", 1)[1]
		return extension

class Crawler():
	def __init__(self, workingDirectory):
		self.workingDirectory = workingDirectory
		
	def crawl(self, processor):
		directory = Directory(self.workingDirectory)
		processor.visit(directory)
			
class FileInfoGenerator():
	def __init__(acceptedExtensions, infoExtansion, infoGeneratorCommand):
		self.acceptedExtensions = acceptedExtensions
		self.infoGeneratorCommand = infoGeneratorCommand
	
	def visit(self, file):
		if(file.getFileExtension in self.acceptedExtensions):
			self.generateInfo(file)
	
	def generateInfo(self, file):
		infoGeneratorCommand = self.infoGeneratorCommand + " " + file.getFilePath()
		try:		
			os.system(infoGeneratorCommand)
		except OSError, (errno, strerror):
			print "Exception occured while generating file informatiom for file: %s, error: %s, message: %s" % (file, errno, strerror)
			
class FilterVisitor():
	def __init__(self, acceptedExtensions, downloaderApplication, outputMap = {}):
		self.acceptedExtensions = acceptedExtensions
		self.downloaderApplication = downloaderApplication
		self.outputMap = outputMap
		
	def visit(self, file):
		log.debug("Found file: %s" % file.getFilePath())
		if(file.getFileExtension() in self.acceptedExtensions):
			log.debug("Processing file file: %s" % file.getFilePath())
			self.processFile(file)
		else:
			log.debug("Ignoring file: %s" % file.getFilePath())
	
	def processFile(self, file):
		processorCommand = self.downloaderApplication + " " + file.getFilePath()
		try:		
			log.debug("Running command: %s" % processorCommand)
			args = [processorCommand]
			process = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE)
			stdoutdata, stderrdata = process.communicate()			
			log.debug("Command: %s output: %s" % (processorCommand, stdoutdata))
			self.outputMap[file.getFilePath()] = stdoutdata
		except OSError, (errno, strerror):
			print "Exception occured while running command: %s, error: %s, message: %s" % (processorCommand, errno, strerror)
			
'''class DeleteVisitor():
	def __init__(acceptedExtensions):
		self.acceptedExtensions = acceptedExtensions
		
	def visit(self, file):
		if(file.getFileExtension in self.acceptedExtensions):
			self.delete(file)
	
	def delete(self, file):
		os.unlink(file.getFilePath)'''


class SubtitlesConverterVisitor():
	def __init__(self, acceptedExtensions, coverterApplication, context):
		self.acceptedExtensions = acceptedExtensions
		self.coverterApplication = coverterApplication
		self.context = context
		
	def visit(self, file):
		if(file.getFileExtension() in self.acceptedExtensions):
			log.debug("Processing file file: %s" % file.getFilePath())
			self.convert(file)
		else:
			log.debug("Ignoring file: %s, not in accepted extensions: %s" % (file.getFilePath(), self.acceptedExtensions))
	
	def convert(self, file): 
		inputSubtitle = file.getFilePath()
		outputSubtitle = file.getFilePath() + ".subrip"
		metaInfo = self.findMatchingFile(inputSubtitle)
		converterCommand = self.coverterApplication + " " + inputSubtitle + " " + outputSubtitle + " " + metaInfo
		try:		
			log.debug("Running command: %s" % converterCommand)
			os.system(converterCommand)
		except OSError, (errno, strerror):
			print "Exception occured while converting file: %s, error: %s, message: %s" % (file, errno, strerror)
			
	def findMatchingFile(self, subtitle):
		for key, value in self.context.iteritems():
			name = key.rsplit(".", 1)[0]
			log.debug("File name: %s, subtitle name: %s" % (name, subtitle))
			if(subtitle.find(name) >= 0):
				return value
		return None

class RenamerVisitor():
	def __init__(self, acceptedExtensions, outputExtensions):
		self.acceptedExtensions = acceptedExtensions
		self.outputExtensions = outputExtensions
	
	def visit(self, file):
		if(file.getFileExtension() in self.acceptedExtensions):
			log.debug("Processing file file: %s" % file.getFilePath())
			self.rename(file)
		else:
			log.debug("Ignoring file: %s, not in accepted extensions: %s" % (file.getFilePath(), self.acceptedExtensions))
	
	def rename(self, file):
		name = file.getFilePath().rsplit(".", 1)[0]
		outputFile = "%s.%s" % (name, self.outputExtensions)
		log.debug("Renaming file: %s to %s" % (file.getFilePath(), outputFile))
		try:
			shutil.move(file.getFilePath(), outputFile)
		except OSError, (errno, strerror):
			print "Exception occured while moving file: %s to %s, error: %s, message: %s" % (file, outputFile, errno, strerror)
		
if __name__ == "__main__":
	moviesExtensions = ("avi", "mkv", "mp4")
	metaInfoReaderResultMap = {}
	parser = OptionParser()
	parser.add_option("-d", "--directory", 
                  help="sets working directory to DIR", metavar="DIR", dest="workingDirectory")
	parser.add_option("-s", "--subdownloader", 
                  help="sets sets subtitles downloader to COMMAND", metavar="COMMAND", dest="downloaderCommand")
	parser.add_option("-m", "--metareader", 
                  help="sets meta movie information reader to COMMAND", metavar="COMMAND", dest="metaInfoRaderCommand")
	parser.add_option("-c", "--converter", 
                  help="sets subtitles converter to COMMAND", metavar="COMMAND", dest="converterCommand")
	parser.add_option("-t", "--testmode", action="store_true", dest="testMode")
	(options, args) = parser.parse_args(sys.argv)	
	logging.basicConfig(level=logging.DEBUG)
 	log = logging.getLogger(__name__)
 	workingDirectory = options.workingDirectory
 	converterCommand = options.converterCommand
 	metaInfoRaderCommand = options.metaInfoRaderCommand
 	testMode = options.testMode
 	if(not workingDirectory):
 		log.error("Working directory (-d / --directory) option is obligatory.")
 		sys.exit()
 	log.debug("Starting in directory %s" % workingDirectory)
	directory = Directory(workingDirectory)
	downloaderCommand = options.downloaderCommand # "/opt/subtitles/periscopen/run.sh"
	if(downloaderCommand):
		log.debug("Downloader dommand %s" % downloaderCommand)		
		downloader = FilterVisitor(moviesExtensions, downloaderCommand)
		directory.accept(downloader)
	if(metaInfoRaderCommand):
		log.debug("Information reader command %s" % metaInfoRaderCommand)		
		metaInfoReader = FilterVisitor(moviesExtensions, metaInfoRaderCommand, metaInfoReaderResultMap)
		directory.accept(metaInfoReader)
		log.debug("Meta info map: %s" % metaInfoReaderResultMap)
	if(converterCommand):
		if(len(metaInfoReaderResultMap)):
			log.debug("Converter command %s" % converterCommand)
			converter = SubtitlesConverterVisitor(("srt"), converterCommand, metaInfoReaderResultMap)
			directory.accept(converter)			
		else:
			log.warn("Ignoring converter command - meta info map is empty - maybe you forgot to pass meta infor reader command ? -m / -metareader")
	log.debug("Test mode = %s" % testMode)
	if(testMode is None):
		rename = RenamerVisitor(("subrip"),("srt"))
		directory.accept(rename)
	else:
		log.debug("Test mode on, not cleaning up / renaming")
	log.debug("\nDone.")	
