# program of magic 8 ball using fumction 

import random

def getanswer(result):
    if result == 1:
        return  'It is a certain'
    elif result == 2:
        return 'it is decidedly so'
    elif result == 3:
        return 'yes'
    elif result == 4:
        return 'Reply hazy try again'
    elif result == 5:
        return 'Ask again later'
    elif result == 6:
        return 'Concentrate and ask again'
    elif result == 7:
        return 'My reply is No'
    elif result == 8:
        return 'Outlook is not good'
    elif result == 9:
        return 'Very doubtful'
    
r = random.randint(1,9)
number = getanswer(r)
print(r ,number)
