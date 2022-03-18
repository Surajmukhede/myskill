#Print characters from a string that are present at an odd index number

Game = input('Enter word')
print('This is actaul name',Game)
size = len(Game)

for i in  range(1,size-1,2):
    print("index[",i,"]",Game)


