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

import first_module
print(first_module.add(67,8))#75
print(first_module.subtract(67,8))#59

importing with alias name:
--------------------------
-->we can also import a module with different name.
-->after importing with the alias name,we have to use that alias name in the code.

import first_module as fm
print(fm.add(67,8))
print(first_module.subtract(67,8))#NameError: name 'first_module' is not defined

importing only need function
----------------------------
-->when we are importing  the few functions from the module can only access that function.
syntax:from (keyword) module_name import(keyword) functions.

from first_module import add,mul
print(add(56,8))#64
print(mul(3,5))#15

importing all functions
-----------------------
-->use all function in that module we have to use(*) to get all of those.
syntax:from(keyword) module_name import(keyword)*

from first_module import*
print(add(45,5))
print(subtract(45,5))
print(mul(45,5))
print(div(45,5))
#o/p:

50
40
225
9.0

import first_module
first_module.display()
#O/P:WelcomeDurga

1.built-in

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
            print(f'you have entered 3 times incorrect pin ur card is blocked)
'''

'''
math
----
-->math module used to work on mathematical functionality.

floor
-----
-->it will round down to the near value
eg
--
'''
import math
print(math.floor(3.78))
'''
ceil
----
it will round-up to the near value
'''
import math
print(math.ceil(3.78))
'''
gcd
---
-->it will find the gcd value
'''
import math
print(math.gcd(24,36))
'''
lcm
---
-->it will find the lcm value
'''
import math
print(math.lcm(24,36))
'''
sqrt
----
-->it will get square root value
'''
import math
print(math.sqrt(25))
'''
factorial
---------
-->it will give factorial value
'''
import math
print(math.factorial(5))

import math
print(math.log(2,3))#log(x,base)
print(math.cos(math.pi))
print(math.pi)
'''
random
------
-->the random module used to get random number

randint
-------
-->used to generate random numbers based on the range
'''
import random
print(random.randint(1,100))
'''
choice
------
-->it will the random value from the given data
import random
'''
import random
color=['black','blue','red','green']
print(random.choice(color))
'''
shuffle
-------
-->it can shuffle the data randomly'''
import random
color=['black','blue','red','green']
random.shuffle(color)
print(color)
'''
uniform
-------
-->it will give the decimal values in a range given
'''
import random
print(random.uniform(1,100))
'''
sys
---
-->sys module is used to get details of python interpreter

version
-------
-->the version of python interpreter
'''
import sys
print(sys.version)
'''
path
----
-->.py path we will get by this function
'''
import sys
print(sys.path)
'''
exit
----
-->this function will exit from the program

import sys
print(sys.exit())

platform
--------
-->it will gives the python run platform
'''
import sys
print(sys.platform)

'''
argv
----
-->it will give the current file run path.
'''
import sys
print(sys.argv)
'''
datatime
--------
-->used to work with date and time
now
---
-->it will give the today time+date
'''
from datetime import datetime
print(datetime.now())
print(datetime.today())


from datetime import datetime
now=datetime.now()
print(now.strftime('%y-%m-%d'))
print(now.strftime("A"))
print(now.strftime("B"))
print(now.strftime('%H:%M:%S'))
print(now.strftime('%y-%m'))
'''
%y-->year
%m-->month
%d-->day
%H-->hour
%M-->minute
%S-->second
%A-->current date
%B-->current month

collections
-----------
-->collections module will provide container type data
which is more powerful than built-in data types(dict,list,tuple)
'''
import collections
data=['apple','banana','orange','banana','pineapple']
print(collections.Counter(data))
'''
deque
-----
-->used to work with list
'''
from collections import deque
how=deque([1,2,3])
how.appendleft(7)
print(how)


from collections import deque
how=deque([1,2,3])
how.extend([4,5,6])
how.extendleft([4,5,6])
print(how)


from collections import deque
how=deque([1,2,3])
how.pop()
print(how)


from collections import namedtuple
data=namedtuple("stu",('name','age'))#namedtuple(typename,field_names)
print(data('durga','18'))

'''
itertools
---------
count:
'''
from itertools import count
c=count(100)
for j in range(5):
    print(next(c))


'''
repeat
------
'''
import itertools
for j in itertools.repeat('python',10):
    print(j)


from itertools import permutations,combinations
data=permutations([1,2,3],2)#(range:,*args:)
print(list(data))

any=combinations([1,2,3],2)
print(list(any))

import platform
print(platform.python_version())
print(platform.python_compiler())
print(platform.machine())
print(platform.processor())



'''
#o/p's:
'''




































