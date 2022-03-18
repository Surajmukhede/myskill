# using get funvtion to access items in dictionary



clothes = {'shirt':4,'pant':2,}

print('i have,' + str(clothes.get('shirt',0)) + 'shirt and only,' + str(clothes.get('pant',0)) + 'pants')

print('i have ,' + str(clothes.get('tshirt',0))) 

# becoz there is no tshirt key in givn list so get function return 0 value