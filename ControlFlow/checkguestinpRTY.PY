# program to check whether guest are coming  in party or not

guest = ['anu','ritesh','akash','piya']
print('Enter the guest name')
name = input()
if name not in guest:
    print('we miss you at party:', name.title())
else :
    print('thanks for coming :', name)