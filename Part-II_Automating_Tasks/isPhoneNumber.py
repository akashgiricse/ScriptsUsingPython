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
