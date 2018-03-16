''' JavaScript Object Notation '''
************************************************************************************
import json

people_string = '''
{
	"people": [
		{
			"name": "Akash Giri",
			"phone": "9721304421",
			"emails": ["akashgiricse@gmail.com", "buggyrango@gmail.com"],
			"is_active": true
		},
		{
			"name": "Mr Rango",
			"phone": "9721304422",
			"emails": null,
			"is_active": false
		}
	]
}
'''

data = json.loads(people_string)

print(type(data))
# <class 'dict'>

print(type(data['people']))
# <class 'list'>

#####################################
''' Python to JSON encoder, decoder

Python <<------------>>	JSON

dict	------------     object
list, tuple ---------	array
str, unicode  ---------- string
int, long, float --------number


'''
######################################

'''
for person in data['people']:
    print(person['name'])

# Akash Giri
# Mr Rango

'''

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)

print(new_string)
'''
{
  "people": [
    {
      "emails": [
        "akashgiricse@gmail.com",
        "buggyrango@gmail.com"
      ],
      "is_active": true,
      "name": "Akash Giri"
    },
    {
      "emails": null,
      "is_active": false,
      "name": "Mr Rango"
    }
  ]
}
'''


*******************************************************************