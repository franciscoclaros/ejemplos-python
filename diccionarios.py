# -*- coding: utf-8 -*-

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


dict['Age'] = 8 # update existing entry
dict['School'] = "DPS School" # Add new entry

for nombre in dict:
    print(dict[nombre])



del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict       # delete entire dictionary


dict = {'Name': 'Zara', 'Age': 7}
print (len(dict))
