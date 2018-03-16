import json

# open json file in the currect directory
with open('states.json') as f:
	#load the file into python object i.e. "data"
    data = json.load(f)

for state in data['states']:
    del state['area_codes']


with open('new_states.json', 'w') as f:
	# convert json data to a file
    json.dump(data, f, indent=2)
