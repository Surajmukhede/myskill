# addition program
num1 = 25
num2 = 30
addition = num1+num2

print("Addition of two number: ",addition)


# Addition using Fucntion

def addition(num1,num2):
    return num1 + num2

sum = addition(10,40)
print('Sum of given number is :',sum)



# Another statergy

def operation(num1,num2):
    if num1 > num2:
        return num1*num2
    if num2 > num1:
        return num1+num2

result= operation(50,10)
print(result)
        

