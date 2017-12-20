# support material for regular expression

import re
# return true if there is a number in the string
def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if text[3]  != '-':
		return False
	for i in range(4,7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8,12):
		if not text[i].isdecimal():
			return False
	return True

message = 'Call me at 485-586-9859 tomorrow. 588-874-8265 is my office.'
for i in range(len(message)):
	chunk = message[i:i+12]
	if isPhoneNumber(chunk):
		print('Phone number found: '+ chunk)

print('Done')

# finding phone number using regular expression i.e. regex

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 485-458-4586')
print (mo.group(1)) # print the first regex group i.e. 485
print (mo.group(2)) # print second regex group i.e 458-4586
print (mo.groups()) # print all groups i.e ('485', '458-4586')

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') # serch for (485) 859-8958 type of number
mo = phoneNumRegex2.search('My phone number is (458) 555-8695')
print(mo.groups())

# using pipe (|) in regex
heroRegex = re.compile(r'Batman|Tine Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group()) # if both regex are found then pipe will return the first one. (i.e. Batman)

# to find regex with specific letter or group of letters
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile and Batman lost a wheel')
print(mo3.group()) # prints Batmobile i.e. first matched regex
print(mo3.group(1)) # prints mobile

# optional matching with question mark
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group()) # prints Batman
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group()) # prints Batwoman

# using optional matching in phoneNumber
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 444-8695')
print(mo1.group()) # prints 444-8695

# matching zero or more with the Star *
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batwowowoman')
print(mo1.group()) # prints Batwowowoman
mo2 = batRegex.search('The adventures of Batman')
print(mo2.group()) # prints Batman

# Matching One or More with the Plus +
batRegex = re.compile(r'Bat(wo)+man') # the regex wo should apear alteast once. 
mo1 = batRegex.search('The adventures of Batwoman')
print(mo1.group())
mo3 = batRegex.search('The adventures of Batman')
if mo3 == None:
	print('True') # prints true

# Matching Specific Repetitions with curly brackets
haRegex = re.compile(r'(Ha){3}') # ha(5,9) will match five to nine HaHaHaHaHa to 9 HaHa pattern 
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

#Greedy and Nongreedy mathing
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group()) # prints HaHaHaHaHa

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa') # prints HaHaHa
print(mo2.group())

# findall() method 
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
print(phoneNumRegex.findall('Cell: 458-859-9689 work: 254-326-8745'))
#prints ['458-859-9689','254-326-8745']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
print(phoneNumRegex.findall('Cell: 125-536-8748 and work : 487-852-6958'))
# pritns [(254,326,8745), (487,852,6958)]

# Making your own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
# prints ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

# negative character class using caret  ^ sign
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))
# prints ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']


# The caret and Dollar sign characters
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('58558545545614'))
# prints <_sre.SRE_Match object; span=(0, 14), match='58558545545614'>

# the Wildcard character "." (dot)

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat. bbbbbat.'))
# prints ['cat', 'hat', 'sat', 'lat', 'mat', 'bat']

# matching everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Akash Last Name: Giri')
print(mo.group(1)) # prints Akash
print(mo.group(2)) # prints Giri

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group()) # prints <To searve man>

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.> ')
print(mo.group()) # prints <To serve man> for dinner.>

# Matching Newlines with the Dot chareter
newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust. \nProtect the innocent. \nUphold the law.')
print(mo.group()) #prints Serve the public trust. 
                  #       Protect the innocent. 
                  #       Uphold the law.
# Case-Insensitive Matching

robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine , all cop.')
print(mo.group()) # prints RoboCop

# Substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo) # prints CENSORED gave the secret documents to CENSORED.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo) # prints A**** told C**** that E**** knew B**** was a double agent.

# Managing Complex Regexes
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? # area code
	(\s|-|\.)?         # separator
	\d{3}              # first 3 digits
	(\s|-|\.)          # separator
	\d{4}              # last 4 digit
	(\s*(ext|x|ext.)\s*\d{2,5})? # extension
	)''',re.VERBOSE)

# Combining re.IGNORECASE , re.DOTALL, and re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)