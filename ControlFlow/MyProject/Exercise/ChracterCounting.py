#program that counts the number of occurrences of each letter in a string

msg = 'i like to coding'
count = {}  # {n} use because ti is disctionary data tupe

for character in msg:
    count.setdefault(character,0)
    count[character]= count[character]+1

print(" these are the total character in given msg", count)


# using ppprint.ppprint() aka pfornat function ; you have to import pprint firstly

import pprint
msg = 'i like to coding'
count = {}  # {n} use because ti is disctionary data tupe

for character in msg:
    count.setdefault(character,0)
    count[character]= count[character]+1

pprint.pprint( count) # it will print  item in cleaner manner
  