'''
List Comprehension
------------------
-->The comprehension is the short from of syntax used to generate a new list from old list
syntax:[expression loop]'''

nums=[1,2,3,4,5]
new_l=[j if j%2==0 else 'odd' for j in nums]
print(new_l)
#o/p:['odd', 2, 'odd', 4, 'odd']

nel_=[i for i in nums if i%2!=0]
print(nel_)
#o/p:[1, 3, 5]
'''
Nested comprehension
--------------------
-->Nested comprehension means an comprehension inside the another comprehension
is called nested comprehension.
syntax:[expression loop_1 and loop_2]'''

match=[[1,2,3],[4,5,6],[7,8,9]]
any_=[i for i in match]
all_=[num for j in match for num in j]
print(any_)
print(all_)
#o/p:
'''
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

new_=[[i*j for j in range(1,6)] for i in range(1,6)]
ne=[i for i in range(1,6)]
print(ne)
print(new_)
#o/p:
'''
[1, 2, 3, 4, 5]
[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]

Generator
---------
-->This generator will generate value one at a time and the pause
it on the position when we are using yield keyword.
-->here we will use yield to get the value
yield keyword
-------------
-->This yield() is used to get the value and will only gives
one value and pauses there itself.


next keyword
------------
-->the next() will retrieve the value.
'''
def gen(n):
    for i in range(1,n+1):
        yield i*i
a=gen(5)
print(next(a))
print(next(a))
#o/p:
'''
1
4

Function
--------
-->return
-->when the return is executed,it will exit for the function.
-->In function will get all values once

generator
---------
-->yield
-->when the yield is executed,it will pause the function
and the next yield is called then it will resume again.
-->In generation will get one at a time.
'''    

















