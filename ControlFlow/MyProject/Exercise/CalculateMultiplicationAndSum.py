# program to calculate multiplicaion and sum of two number

def multiplicationorsum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
    
result= multiplicationorsum(20,30)
print(result)

result = multiplicationorsum(40,30)
print(result)