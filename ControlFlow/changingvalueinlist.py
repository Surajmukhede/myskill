#Changing Values in a List with Indexes

spam = ['cat', 'bat', 'rat', 'elephant']
spam[2]= 'lion' # chjange by direct apply variable

spam[1]= spam[3]   # assign a value form index 

print(spam)

# list concentation and list replication 

colour = ['black','blue','yellow','green'] + ['night','sky','grass']
print(colour)

# list replication

colour = ['black','blue','yellow','green'] *2
print(colour)

# adding another list to exiting list
colour = ['black','blue','yellow','green']

colour = colour + ['white','grey']
print(colour)
