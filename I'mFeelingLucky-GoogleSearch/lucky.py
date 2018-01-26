#~ python3
# lucky.py - Opens several Google serch results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page

# The command line arguments will be stored as strings in a list in sys.argv
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# Retrive top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))