#!/usr/bin/python

import os, sys

def downloadSubtitles(downloader, moviePath, movieFile):
	movie = moviePath + "/" + movieFile
	print "Downloading subtitles for movie %s" % movie 
	downloaderCommand = downloader + " " + movie
	try:		
		os.system(downloaderCommand)
	except OSError, (errno, strerror):
		print "Exception occured while downloading subtitles for movie: %s, error: %s, message: %s" % (file,errno,strerror)

def convertSubtitles(converter, subtitlePath, subtitleFile):
	inputSubtitle = subtitlePath + "/" + subtitleFile
	outputSubtitle = subtitlePath + "/" + subtitleFile + ".subrip"
	converterCommand = converter + " " + inputSubtitle + " " + outputSubtitle
	try:		
		os.system(converterCommand)
	except OSError, (errno, strerror):
		print "Exception occured while converting file: %s, error: %s, message: %s" % (file,errno,strerror)

def removeFile(subtitlePath, subtitleFile):
	subtitle = subtitlePath + "/" + subtitleFile
	try:		
		os.remove(subtitle)
	except OSError, (errno, strerror):
		print "Exception occured while removing file: %s, error: %s, message: %s" % (file,errno,strerror)

def renameFile(subtitlePath, subtitleFile, extension):
	originalSubtitle = subtitlePath + "/" + subtitleFile
	subtitleName = subtitleFile.rsplit(".")[0]
	subtitleExtensionPart1 = subtitleFile.rsplit(".")[1]
	renamedSubtitle = subtitlePath + "/" + subtitleName + "." + subtitleExtensionPart1 + "." + extension
	try:		
		os.rename(originalSubtitle, renamedSubtitle)
	except OSError, (errno, strerror):
		print "Exception occured while removing file: %s, error: %s, message: %s" % (file,errno,strerror)

def isMovieFile(movieFilesExtensions, fileName):
	
directory = sys.argv[1]
downloader = "/opt/subtitles/periscopen/run.sh"
converter = "/opt/subtitles/sub2srt-0.5.2/run.sh"
print "Working directory: %s" % directory
# download subtitles
for root, dirs, files in os.walk(directory):
	for file in files:
		if file.endswith('.avi') or file.endswith('.mkv'):
			downloadSubtitles(downloader, directory, file)
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
