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

""" OUTPUT is 
The current folder is /home/rango/ExampleFolder
SUBFOLDER OF /home/rango/ExampleFolder: subFolder
FILE INSIDE /home/rango/ExampleFolder: doc.txt

The current folder is /home/rango/ExampleFolder/subFolder
SUBFOLDER OF /home/rango/ExampleFolder/subFolder: subSubFolder
FILE INSIDE /home/rango/ExampleFolder/subFolder: subDoc.txt

The current folder is /home/rango/ExampleFolder/subFolder/subSubFolder
FILE INSIDE /home/rango/ExampleFolder/subFolder/subSubFolder: subSubDoc.txt
"""


# Compressing Files with the zipfile Module
import zipfile, os
# create object named "exampleZip"
exampleZip = zipfile.ZipFile('/home/rango/Downloads/Create-a-blog.zip')
print(exampleZip.namelist()) # prints all the files and folderes contained in zip file
"""
for example 
['Navigation.html', 'blog/', 'blog/css/', 'blog/css/bootstrap.min.css',
'blog/css/font-awesome.min.css', 'blog/Header.html', 'blog/Footer.html']

"""
spamInfo = exampleZip.getinfo('Navigation.html')
#prints 3926
print(spamInfo.file_size)
#prints 902
print(spamInfo.compress_size)
#prints 
#compressed file is 4.35x smaller!
print('compressed file is %sx smaller!' %(round(spamInfo.file_size/spamInfo.compress_size, 2)))
exampleZip.close()

# Extracting from ZIP Files

