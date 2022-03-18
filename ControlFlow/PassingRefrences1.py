
#References are particularly important for understanding how arguments
#get passed to functions. When a function is called, the values of the argu-
#ments are copied to the parameter variables

def name(student):
    student.append('kishor')

name1 = ['asha','pravin']  # storing result
name(name1)                # calling given variable
print(name1)

# even though student and name1 contains seperate reference they both refer to same list 