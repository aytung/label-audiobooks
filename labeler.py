# find all folders
# then, for each of those folders, 
# find all of the filenames
# then, for each of those filenames, you
# need to find the 

import os
import shelve
import eyed3

shelffile = shelve.open('formattedAudiobooks')
formattedString = 'formattedAudiobooks'

formattedAudiobooks = None 
if formattedString not in shelffile:
	formattedAudiobooks  = []
	shelffile[formattedString] = formattedAudiobooks
else:
	formattedAudiobooks = shelffile[formattedString]
curDir = os.getcwd()
audiobooks = [audiobook for audiobook in os.listdir() if os.path.isdir(os.path.join(curDir, audiobook))]
# also want to keep a file that has a list of formattedAudiobooks
for audiobook in audiobooks:
	audioFiles = [audiobook + "/" + audioFile for audioFile in os.listdir(audiobook)]

	audioFiles.sort()
	audioFiles = [eyed3.load(audioFile) for audioFile in audioFiles]
	for track_num, audioFile in enumerate(audioFiles, 1):
		audioFile.tag.album = audiobook
		# for Audiobooks
		audioFile.genre = 'Audiobook'
		audioFile.tag.track_num = track_num
		# for Podcasts
		audioFile.genre = 'Podcast'

		audioFile.tag.save()


	formattedAudiobooks.append(audiobook)



shelffile.close()