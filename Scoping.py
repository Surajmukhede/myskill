# local Scope : parameter and variable exist inside function
# global scope : exist in outside function


# local variable cannot access in global scope


def fruit():
    vegitable = 'apple'


fruit()
print(vegitable) # so we cant access local variable in global

# local scope variable canot access in other local scope

def spam():
    eggs = 99
    bacon()
    print(eggs) 

def bacon():
    ham = 101
    eggs =0

spam()