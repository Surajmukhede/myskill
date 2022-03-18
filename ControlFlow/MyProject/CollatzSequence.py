# finding given number is odd or even

number = int(input())

def Collatz(number):
    if number % 2 == 0:
        print('Given number is even ')
    else:
        print('given number is odd')

    return 'this is the result of given number'


print(Collatz(number))
