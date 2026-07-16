'''===>Tokens
1.keyword: Tokens are smallest individual parts or units in the program
num=0
if
for
else
return
while
and
in'''
    
'''2.Identifiers
----------------
function name
class name



3.Operators:+,_,=
4.Literal:int,str,tuple,list

OPERATORS
----------------------------
1.ARITHMATIC:-,=,/,%,*,**'''
num=8
num_2=7
print(num + num_2)
print(num - num_2)
print(num * num_2)
print(num ** num_2)
print(num % num_2)
print(num / num_2)


'''2.ASSIGNMENT OPERATOR:+=,-=,%=,/='''
num = 8
num_2 = 7
num_2 -=1
print(num_2)


'''3.COMPARISON:==,!=,<=,>=,<,>'''
num = 8
num_2 = 7
print(num == num_2)
print(num <= num_2)
print(num >= num_2)
print(num != num_2)
print(num > num_2)
print(num < num_2) 


'''4.LOGICAL:and or not'''
num = 78
num_2 = 89
print(num < num_2 and num_2 < 100)
print(num < num_2 or num_2 < 100)
print(not(num < num_2 and num_2 < 100))



'''5.IDENTITY:is,is not'''
num = 9
num_2 = 9
print(num is num_2)#look for object
print(num == num_2)#values equal or not



so = 1
how =1
print(id(so))#id will check memory address
print(id(how))
print(so is how)
print(so == how)


num_3 = [1,2]
num_4 = [1,2]
print(id(num_3))
print(id(num_4))
print(num_3 is num_4)
print(num_3 == num_4)



'''6.MEMBERSHIP:in,not in'''
so = [1,2,3,4,5]
print(7 in so)



'''7.BITWISE: &,|,^,<<,>>'''
print(5 & 3)
print(5 | 3)
print(5 >> 3)
print(5 << 3)



 

 
