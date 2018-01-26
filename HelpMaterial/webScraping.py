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

#########################################
# Finding an Element with select() Method

# Some Examples of CSS Selectors

soup.select('div') :: All elements named <div>
soup.select('#author') :: The element with an id attribute of author
soup.select('.notice') :: All elements that use a CSS class attribute named notice
soup.select('div span') :: All elements named <span> that are within an element named <div>
soup.select('div > span') :: All elements named <span> taht are directly within an element named <div>
soup.select('input[name') :: All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]') :: All elements named <input> that have an attribute named type with value button

###########################################################

# the select() method will return a list of Tag objects.
################################################3

# for example here is an example.html

# <!-- This is the example.html example file. -->
# <html>
# <head>
# 	<title>The Website Title</title>
# </head>
# <body>
# 	<p>Download my <strong>Python</strong> book from <a href="http://
# 	inventwithpython.com">my website</a>.</p>
# 	<p class="slogan">Learn Python the easy way!</p>
# 	<p class="slogan">Learn Python the hard way!</p>
# 	<p>By <span id="author">Al Sweigart</span></p>
# </body>
# </html>

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select('#author')
# prints <class 'list'>
print(type(elems))
# prints 1
# that is there is one Tag object in the list
print(len(elems))
# prints <class 'bs4.element.Tag'>
print(type(elems[0]))
# prints Al Sweigart
print(elems[0].getText())
# prints <span id="author">Al Sweigart</span>
print(str(elems[0]))
# prints {'id': 'author'}
print(elems[0].attrs)

pElems = exampleSoup.select('p')

# prins 4
print(len(pElems))
# prins {'class': ['slogan']}
print(pElems[2].attrs)
# prints <p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>
print(str(pElems[0]))
# prints Download my Python book from my website.
print(pElems[0].getText())
# prints <p class="slogan">Learn Python the easy way!</p>
print(str(pElems[1]))
# prins Learn Python the easy way!
print(pElems[1].getText())


#######################################################33
# Getting Data from an Element's Attributes
###########################################33
import bs4

soup = bs4.BeautifulSoup(open('example.html'), "html.parser")
# store the first match element in spanElem.
spanElem = soup.select('span')[0]
# Print <span id="author">Al Sweigart</span>
print(str(spanElem))
# prints author
print(spanElem.get('id'))
# prints True
print(spanElem.get('some_nonexistent_addr') == None) 
# prins {'id': 'author'}
print(spanElem.attrs)


#######################################################
# Controlling the Browser with the selenium Module
#####################################
# Starting a Selenium-controlled Browser

from selenium import webdriver
# It will open firefox
# Please add "geckodriver" to your /local/bin folder
# Choose your "gechodriver" here https://github.com/mozilla/geckodriver/releases
browserFirefox = webdriver.Firefox()

# It will open Chrome
# Please add "chromedriver" to your /local/bin folder
# Choose your "chromedriver" here https://chromedriver.storage.googleapis.com/index.html?path=2.35/
browserChrome = webdriver.Chrome()

# prints <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
type(browserFirefox)
# will open firefox with the given site
browserFirefox.get('http://inventwithpython.com')

###################################33
# Finding Elements on the Page

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')


try:
	elem = browser.find_element_by_class_name('card-img-top')
	print('Found <%s> element with that class name! ' % (elem.tag_name))
except:
	print('Was not able to find an element with that name.')
# will print Found <img> element with that class name!


#######################33
# Clicking the Page
##############

from selenium import webdriver

#open 4chan site in chrome
browser = webdriver.Chrome()
browser.get('https://www.4chan.org')
# click on Technology link on 4chan home page
linkElem = browser.find_element_by_link_text('Technology')
linkElem.click() 
# Click on popup window for accepting their terms and condition
acceptElem = "//button[@data-cmd='ok-disc']"
browser.find_element_by_xpath(acceptElem).click()

###############################333
# Filling Out and Submitting Forms
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.reddit.com/')

userNameElem = browser.find_element_by_name('user')
userNameElem.send_keys('Your_username_here')
passwordElem =browser.find_element_by_name('passwd')
passwordElem.send_keys('Your_Password_here')
passwordElem.submit()

############################################
# Sending Special Keys
###########################333
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.reddit.com/')

htmlElem = browser.find_element_by_tag_name('html')
# moves to the bottom of the page
htmlElem.send_keys(Keys.END)
# moves at the top
htmlElem.send_keys(Keys.HOME)

####################33333
# Clicking Browser Buttons
browser.back() # Clicks the Back button
browser.forward() # Clicks the Forward button
browser.refresh() # Clicks the Refresh/Reload button
browser.quit() # Clicks the Close Window button

