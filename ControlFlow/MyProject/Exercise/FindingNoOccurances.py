#  count the number of occurrences

def countnumberofoccurance(number, x):
	count = 0
	for element in number:
		if element == x:
			count = count + 1
	return count


number = [1,1,2,3,4,1,1]
x = 1
print('finding occurance of given number is: ',x, '\nnumber of occurance of given element:',countnumberofoccurance(number, x))