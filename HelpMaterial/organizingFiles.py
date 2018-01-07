# Orgainzing Files using Python

# The shutil Module (or shell utilities)

# copying files and folders
# in python3 shell
>>> import shutil, os
# shutil.copy will copy single file
shutil.copy('/home/rango/Downloads/LinuxBackupLog.txt', '/home/rango/Desktop')
'/home/rango/Desktop/LinuxBackupLog.txt'
>>> shutil.copy('/home/rango/hello.txt', '/home/rango/Downloads/LinuxBackupLog.txt')
'/home/rango/Downloads/LinuxBackupLog.txt'
>>>
# shutil.copytree() will copy entire folder.

# Moving and Renaming Files and Folders
>>> shutil.move('/home/rango/hello.txt', '/home/rango/Desktop')
'/home/rango/Desktop/hello.txt' # file will move to this location
>>>

# Permanently Deleting Files and Folders
import os
for filename in os.listdir():
	if filename.endswith('.rxt'):
		os.unlink(filename)
		print(filename)
		# will delete all files having extention '.rxt'
# os.rmtree() will delete entire folder

# Safe Deletes with the send2trash module
import send2trash
baconFile = open('bacon.txt', 'a') # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')
# sends 'bacon.txt' to trash


# Walking a Directory Tree

"""
Suppose this is a Directory Tree
ExampleFolder
	subFolder
		subSubFolder
			subsubDoc.txt
		subDoc.txt
	doc.txt
"""
import os
for folderName, subfolders, filenames in os.walk('/home/rango/ExampleFolder'):
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': ' + filename)

	print('')