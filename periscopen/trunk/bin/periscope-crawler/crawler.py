#!/usr/bin/python


import os, sys
import logging
import subprocess
import shutil

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
	logging.basicConfig(level=logging.DEBUG)
 	log = logging.getLogger(__name__)
 	workingDirectory = sys.argv[1]	
 	log.debug("Starting in directory %s" % workingDirectory)
	directory = Directory(workingDirectory)
	downloaderCommand = sys.argv[2] # "/opt/subtitles/periscopen/run.sh"
	log.debug("Downloader dommand %s" % downloaderCommand)
	moviesExtensions = ("avi", "mkv", "mp4")
	downloader = FilterVisitor(moviesExtensions, downloaderCommand)
	directory.accept(downloader);
	metaInfoRaderCommand = sys.argv[3]
	log.debug("Information reader command %s" % downloaderCommand)
	metaInfoReaderResultMap = {}
	metaInfoReader = FilterVisitor(moviesExtensions, metaInfoRaderCommand, metaInfoReaderResultMap)
	directory.accept(metaInfoReader);
	log.debug("Meta info map: %s" % metaInfoReaderResultMap)
	converterCommand = sys.argv[4]
	log.debug("Converter command %s" % converterCommand)
	converter = SubtitlesConverterVisitor(("srt"), converterCommand, metaInfoReaderResultMap)
	directory.accept(converter);
	rename = RenamerVisitor(("subrip"),("srt"));
	directory.accept(rename);
	log.debug("\nDone.")	
