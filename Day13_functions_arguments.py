'''
#defult argument value
----------------------
ex:no automatically used parameters if no arguments passed'''

def any_(age,edu,name):
    print(name)
any_('durga',50,'b.tech')
#o/p:b.tech

#ex: passed arguments

def any_(age,edu,name):
    print(name)
any_( name='durga',age=21,edu='b.tech')
#o/p:durga

'''
#variable-length positional arguments
-------------------------------------
#i.*args
--------
--->we can pass tuple of arguments and stored in a single parameter bt just adding* before the parameter
--->*single take tuples
'''
#ex:we want particaler value

def all_(*nums):
    print(nums[1])
all_(10,30,20,8)
#o/p:30

#ex:adding

def all_(*nums):
    print(nums[1]+nums[3])
all_(10,30,20,8)
#o/p:38

#ex:print all list


def all_(*nums):
    print(nums)
all_(10,30,20,8)
#o/p:(10, 30, 20, 8)

'''
#ii.**kargs
-----------
--->by pass keyword arguments in the arguments,will get it as dic just adding ** before the parameter
--->and can access by using dc methods...
ex:'''

def dct(**all_in):
    for key,val in all_in.items():
        print(key,':',val)
dct(name = 'teja',age ='56',role ='mentor')
#o/p:
'''
name : teja
age : 56
role : mentor
'''

#both using *args and **kargs
'''
ex:
'''
def dct_nums(*args,**kargs):
    print(args)
    print(kargs)
dct_nums(12,33,56,name='vyshnavi',age=50,edu='b.tech')
#o/p:
'''
(12, 33, 56)
{'name': 'vyshnavi', 'age': 50, 'edu': 'b.tech'}

------------------------------------------------------
--scope of the varibles---
i.local variable :outside the varible
ex:
'''
num_2 = 89
def nums(num_2):
    num = 90
    print(num)
    print(num_2)
nums(num_2)
print(num_2)
#o/p:
'''
90
89
89
'''


#fabanocci

limit_ = int(input('enter the limit: '))
num = 0
num_2 = 1
def fibonocci(limit_,num,num_2):
    print(num,num_2,end=' ')
    for j in range(1,limit_+1):
        num_3 = num+num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=' ')
fibonocci(limit_,num,num_2)
#o/p:
'''
enter the limit: 10
0 1 1 2 3 5 8 13 21 34 55 89 


---passing by value--

ex:'''
def any_(a,b):
    print(a)
    print(b)
any_(23,34)
#o/p:
'''
23
34

--passing by reference----

ex:'''

def any_(num,num_2):
    print(num)
    print(num_2)
any_(num = 8 , num_2 = 9)
'''
#o/p:
8
9
'''

