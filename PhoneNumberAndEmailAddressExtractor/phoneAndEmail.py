#! python2
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# phoneNumber regex
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? # area code
	(\s|-|\.)?         # separator
	(\d{3})            # first 3 digits
	(\s|-|\.)          # separator
	(\d{4})            # last 4 digit
	(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
	)''',re.VERBOSE)

# email regex
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ #username
	@                 # @ symbol
	[a-zA-Z0-9.-]+    # domain name
	(\.[a-zA-Z]{2,4}) # dot-something
	)''', re.VERBOSE)