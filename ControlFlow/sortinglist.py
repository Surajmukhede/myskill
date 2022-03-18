# sorting list using sort method

from unicodedata import name


Num = ['A','b','C','g','T']
Num.sort()
print(Num)
# 1. you cannot sort lists that have both number values and string
#    values in them, since Python doesn’t know how to compare these values
# 2. sort() uses “ASCIIbetical order” rather than actual alphabetical
#    order for sorting strings. This means uppercase letters come before lower-
#    case letters. Therefore, the lowercase a is sorted so that it comes after the
#    uppercase Z.

# sorting the list in alphabitcally 

nam = ['A','a','P','z','R']
nam.sort(key=str.lower)

print(nam)