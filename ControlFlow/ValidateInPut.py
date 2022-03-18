# Validate wether given user data are valid or not 

## checking database wether givem name is available or not 
while True:
    print('Please enter your name ')
    name = input()
    if name.istitle():
        print('welcome,',name )
        break
    print('kindly enter your name in title case')

# ask user to create password for future login

while True:
    
    print('Please set your password')
    password = input()
    if password.isalnum():
        print('password is created successfully!', 'Suraj Mukhede')
        break
    
    print('Your password should contain only character and number')

