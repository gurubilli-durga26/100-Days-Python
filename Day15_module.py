
'''
modules
-------
-->modulus are the python code which is saved in (.py) that contain functions,variables,classes.

types
-----
1.built-in
-->the build-in modules that are already designed which comes with python when we are installing.
eg
--
1.math
2.sys
3.os
4.random

2.user-defined
--------------
-->the user-define modules are created by the programmer.
syntax:import(keyword)module_name
'''
import first_module
print(first_module.add(67,8))#75
print(first_module.subtract(67,8))#59
'''
importing with alias name:
--------------------------
-->we can also import a module with different name.
-->after importing with the alias name,we have to use that alias name in the code.
'''
import first_module as fm
print(fm.add(67,8))
print(first_module.subtract(67,8))#NameError: name 'first_module' is not defined
'''
importing only need function
----------------------------
-->when we are importing  the few functions from the module can only access that function.
syntax:from (keyword) module_name import(keyword) functions.
'''
from first_module import add,mul
print(add(56,8))#64
print(mul(3,5))#15
'''
importing all functions
-----------------------
-->use all function in that module we have to use(*) to get all of those.
syntax:from(keyword) module_name import(keyword)*
'''
from first_module import*
print(add(45,5))
print(subtract(45,5))
print(mul(45,5))
print(div(45,5))
#o/p:
'''
50
40
225
9.0
'''
import first_module
first_module.display()
#O/P:WelcomeDurga

'''1.built-in'''

import random
print(random.randint(1000,100000))#it will generate random b/w given range
#O/P:12963
import math
print(math.sqrt(25))
#5
import sys
print(sys.version)

#ATM OTP Generator
details={'name':'Durga','ATM PIN':'1234'}
import random
remain=3
while remain>0:
    pin=input('Enter pin number:')
    if pin==details['ATM PIN']:
        otp=random.randint(1000,9999)
        print(otp)
        user_otp=int(input('Enter user otp:'))
        if user_otp==otp:
            opt=int(input('Enter option \n1.withdraw \n2.deposit'))
    else:
        remain-=1
        if remain>0:
            print(f'incorrect pin entered and you have {remain}')
        else:
            print(f'you have entered 3 times incorrect pin ur card is blocked')

