#String with a file path
import os
os.path.join('usr', 'bin', 'spam')
# prints string i.e. 'usr/bin/spam'

# join names from a list of filenames to the end of a folder's name:
myFiles = ['account.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
	print(os.path.join('rango/Pictures', filename))
#prints string i.e.
# rango/Pictures/account.txt
# rango/Pictures/details.csv
# rango/Pictures/invite.docx


# current working directory
print(os.getcwd())
# prints current directory, in my case it's '/home/rango/ScriptsUsingPython/HelpMaterial'
os.chdir('/home/rango/Pictures')
print(os.getcwd()) # prints /home/rango/Pictures
"""
# Creating New Folder with os.makedirs()
os.makedirs('/home/rango/directory1/subdir/subsubdir/mail.txt')
# will create directory "/home/rango/directory1/subdir/subsubdir/mail.txt"
"""

# Handling Absolute and Relative Paths
os.path.abspath('.')
# returns '/home/rango/ScriptsUsingPython/HelpMaterial'

os.path.abspath('./Pictures')
# returns '/home/rango/Pictures'

os.path.isabs('.')
# returns False

os.path.isabs(os.path.abspath('.'))
# returns True

os.path.relpath('/home/rango', '/home')
# returns 'rango'

os.path.relpath('/home/rango', '/home/rango/Desktop/Books')
# returns '../..'

filePath = '/home/rango/Desktop/Books'
os.path.dirname(filePath)
# returns '/home/rango/Desktop'
os.path.basename(filePath)
# returns 'Books'
os.path.split(filePath)
# returns ('/home/rango/Desktop', 'Books') i.e. both dirname and basename.
filePath.split(os.path.sep)
# returns ['', 'home', 'rango', 'Desktop', 'Books']
'/rango/bin'.split(os.path.sep)
# returns ['', 'rango', 'bin']

# Finding File Sizes and Folder Contenets
os.path.getsize('/home/rango/Desktop/Books/automate-the-boring-stuff-with-python-2015-.pdf')
# returns 17449893 in bytes
os.listdir('/home/rango/Desktop/Books')
# returns ['DjangoBook', 'automate-the-boring-stuff-with-python-2015-.pdf']

totalSize = 0
for filename in os.listdir('/home/rango/Desktop/Books'):
	totalSize = totalSize + os.path.getsize(os.path.join('/home/rango/Desktop/Books', filename))
print(totalSize) # prints 17453989 

# Checking Path Valitidy
os.path.exists('/home/rango')
True
os.path.exists('/home/rangodango')
False
os.path.isfile('/home/rango/Desktop')
False
os.path.isfile('/home/rango/Desktop/StartDjango.txt')
True
os.path.exists('/media/rango/Windows')
False # when unmounted
os.path.exists('/media/rango/Windows')
True # when mounted

# File Reading/Writing Process
# Opening Files with the open() function
helloFile = open('/home/rango/hello.txt') # stores the file object in Read Mode
helloContent = helloFile.read()
print(helloContent) # prints content inside the hello.txt file

# writing to files
# in python intetective shell
>>> import os
>>> helloFile = open('hello.txt','w') # open hello.txt in write mode i.e. using 'w'
>>> helloFile.write('entered into shell \n')
20
>>> helloFile.close()
>>> helloFile = open('hello.txt', 'a') # open fine in append mode so that it will append text and not replace
>>> helloFile.write('Hello again.')
12
>>> helloFile.close()
>>> helloFile = open('hello.txt')
>>> content = helloFile.read()
>>> helloFile.close()
>>> print(content)
entered into shell 
Hello again.
>>> 






