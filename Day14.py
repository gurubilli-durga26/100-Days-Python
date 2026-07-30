'''
#Anonymous function
-------------------
-->Anonymous function is a function that don't any name
-->this also called as Lambda Function
-->lambda function will take n number arguments but only one expression

syntax:lambda arguments:expression
'''
#signal arguments
so=lambda a:a+10
print(so(2))
#o/p:12

#mul arugments
so=lambda a,b,c:a+b+c
print(so(2,45,6))
#o/p:53

#factorial
def num(n):
    if n==1:
        return 1
    return n*num(n-1)
print(num(5))
#o/p:120
'''
map()
----
-->the map function will be applied on the given function of each and every element of an itterable.'''
nums=[1,2,3,4,5,6]
so=list(map(lambda x:x*x,nums))
print(so)
#o/p:[1, 4, 9, 16, 25, 36]
'''
filter()
--------
-->filter() function will only consider if the condition is true,then it will keep that values.
nums=[1,2,3,4,5,6]
so=list(filter(lambda x:x%2==0,nums))
print(so)
#o/p:[2, 4, 6]
'''
from functools import reduce
nums=[1,2,3,4,5]
so=reduce(lambda x,y:x+y,nums)
print(so)
