#! python3
# support material for Web Scraping

import webbrowser

# open web browser to a specified url
webbrowser.open('https://akashgiricse.github.io/')

#########################################################################
# Downloading Files from the web with the requests Module
##################################################
# Downloading a Web Page with the requests.get() function

# "res" holds the downloaded web page as a string
>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
>>> type(res)
<class 'requests.models.Response'>
# for checking the request state
# status code for "OK" in the HTTP protocol is 200.
# Status code for "Not Found" in the HTTP protocol is 404.
>>> res.status_code == requests.codes.ok
True
>>> len(res.text)
178981
>>> print(res.text[:250])
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Proje
>>> 
###########################################
# Checking for Errors
>>>> import requests
>>> res = requests.get('https://akashgiricse.github.io/page_does_not_exist')
>>> res.raise_for_status()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.5/dist-packages/requests/models.py", line 935, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://akashgiricse.github.io/page_does_not_exist
>>>
################################################
# Always try and except method to insure that the connection was stablish or not to the URL
import requests

res = requests.get('https://akashgiricse.github.io/page_does_not_exist')
try:
	res.raise_for_status()
except Exception as exc:
	print('There was a problem: %s' %(exc))

# output is:
# There was a problem: 404 Client Error: Not Found for url: https://akashgiricse.github.io/page_does_not_exist

###########################################################################
# Saving Downloaded Files to the Hard Drive

import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
# Open the file in write binary mode by passing the string 'wb' as the second argument to open()
# Event if the page is in plain-text, you need to write binary data instead of text data in order0 to 
# maintain the Unicode encoding of the text
playFile = open('RomeoAndJuliet.txt', 'wb')
# The iter_content() method returns "chunks" of the content on each iteration through the loop.
# Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain.
# in this case 100,000 bytes
for chunk in res.iter_content(100000):
	playFile.write(chunk)

playFile.close()


######################################################################
# Parsing HTML with the BeautifulSoup Module

########################################3
# Creating a BeautifulSoup Object from HTML

import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
# prints <class 'bs4.BeautifulSoup'>
print(type(noStarchSoup))

# you can also load an HTML file from your hard drive by passing a File object to bs4.BeautifulSoup()
# for example, there is a file on my home directory named example.html
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))

