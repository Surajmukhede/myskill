

from audioop import add
sum = 10

def additionFirstNNumbers(n):
    sum = 0
    for i in range(1,n + 1):
        sum = sum + i
    return sum

sum = additionFirstNNumbers(2)
print(sum)

def checkEvenOdd(number):
    if number % 2 == 0:
        print("Given Number is Even")
    else:
        print("Given Number is Odd")


def functionWithNoInputButOutput():
    name = 'Suraj'
    return name


name  = functionWithNoInputButOutput()
print(name)
# checkEvenOdd(10)
# checkEvenOdd(9)
# if 10 % 2 == 0:
#     print("Given Number is Even")
# else:
#     print("Given Number is Odd")
# if 9 % 2 == 0:
#     print("Given Number is Even")
# else:
#     print("Given Number is Odd")