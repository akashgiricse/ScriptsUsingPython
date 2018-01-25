#! python3
# mapIt.py - Launches a map in the browser using an address from 
# command line or clipboard.

import webbrowser, sys

if len(sys.argv) >1:
	# Get the address from command lilne.
	address = ' '.join(sys.argv[1:])

else:
	# Get the address from clipboard.
	address = pyperclip.paste()

webbrowser.open('https://www.google.co.in/maps/place/' + address)