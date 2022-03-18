# it is immppsible to make change in string data type although it can be done
# by slicing and concanteation


name = 'suraj mukhede'
newname = name[0:5]+ ' '+ 'ramakant'+ name[5:14]
print(newname)

# orginal string not modified 

# although list is mutable
num = ['5','6','6']
#print(num)
num =['10','15','20']
print(num)

#If you wanted to actually modify the original list then
number = ['4','6','10']
del number[2]
del number[1]
del number[0]
number.append(11)
number.append(20)
number.append(30)

print(number)