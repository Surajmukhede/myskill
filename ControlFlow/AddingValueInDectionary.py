


Fav_food = {'Akash':'Apple','Vikas':'Guava','Nila':'Banana'}

while True:
    print('enter a name: (blank to quit)')
    name = input
    if name == ' ':
        break
    if name in Fav_food:
        print(Fav_food[name] + 'is the favorites of ', name )
    else:
        print('I dont have sufficient data')

        print('What is his/her favourite food')
        food = input()
        Fav_food[name] = food

        print('Data Updated')