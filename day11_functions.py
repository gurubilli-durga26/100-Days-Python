'''
Functions:
-->function is block that can be executes when we call it.
-->to avoid the repeated lines of codes.
def function_name(parameters):
     --------
     --------
     --------
function_name(arguments)


Types of functions:
1.Built-in
eg:
print()
len()
max()
min()

2.User-define
-->user-define are the functions that are develop by the user
#addition
'''
num=56
num_2=89
def total(num,num_2):
    print(num+num_2)
total(num,num_2)
total(1,2)
'''
#sub'
'''
num=56
num_2=76
def total(num,num_2):
    print(num-num_2)
total(num,num_2)
total(5,3)
'''
#mul
'''
num=56
num_2=76
def total(num,num_2):
    print(num*num_2)
total(num,num_2)
total(5,3)
'''
required arugments:
-->we have to pass same number arguments that match in the parameters

'''
num=56
num_2=89
def total(num,num_2):
    print(num+num_2)
total(num,num_2)
total(1,2,3)#error
'''
positional arguments:
-->it does not matter how we are passing the variable,if we assign the value to that variable in the calling.
eg1:
'''
def name_(name_,name):
    print(name)
    print(name_)
name_(name='Durga',name_='Gurubilli')
'''
eg2:
'''
def position(a,c,b,e,d):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
position(a=0,b=9,c=8,d=7,e=6)
    
    
 
