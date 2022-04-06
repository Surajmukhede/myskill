# using random modules 

import random

for i in range(0,100):
    print(random.randint(10,20))



#using sys modules

import sys

while True:
    print('when you complete your graduation')
    date = int(input())
    if date == 2016:
        sys.exit

    else:
        print('wrong selection')
