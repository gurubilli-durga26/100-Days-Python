'''set
   ---
-->set is an unordered collection.
-->set do not allows duplicate values inside it.
-->set is mutable.
-->set is represented in{}.'''

do={1,2,2,3}
print(do)#{1, 2, 3}

#creating a empty set
so=set()
print(type(so))#<class 'set'>

'''methods
   -------
1.update
2.add
3.remove
4.discard  
5.pop
6.operations
1.update:use to add new value into set
syntax-->variable_name.update(iterable)'''
do={1,2,3}
do.update('python')
print(do)#{'t', 1, 2, 3, 'h', 'n', 'y', 'o', 'p'}it is unordered

'''2.add:use to add new value into set
syntax-->variable_name.add(value)'''
do={1,2,3}
do.add('python')
print(do)#{1, 2, 3, 'python'}

'''3:remove:used to del the value from the set,incase if the value is not present in the set will get the keyError
syntax-->variable_name.remove(value)'''
do={1,2,3}
do.remove(4)
print(do)#KeyError: 4 value is not there in set

do={1,2,3,4}
do.remove(4)
print(do)#{1, 2, 3}

'''4.discard:used to del the value from the set,but never give any error incase value is not present inside the set
syntax-->variable_name.discard(value)'''
do={1,2,3}
do.discard(4)
print(do)#{1, 2, 3} it not throw the error

'''5.pop:used to del the value but the this pop() will take 0 arugments inside it
syntax-->variable_name.pop()'''
do={1,2,3}
do.pop()
print(do)#{2, 3}

'''6.operations
------------
1.union:gives all sets value together but no duplicates'''

do={1,2,3}
so={3,4,5}
print(do|so)#{1, 2, 3, 4, 5}.(| its is a union symbol)
print(do.union(so))#{1, 2, 3, 4, 5}

'''2.intersection:common values in both sides'''
do={1,2,3}
so={3,4,5}
print(do&so)
print(do.intersection(so))#{3}
                          #{3}

'''3.difference:'''
do={1,2,3}
so={3,4,5}
print(so-do)#{4, 5}
print(so.difference(do))#{4, 5}


'''TYPE CONVERSION
---------------
int:
---
1.string--str()'''
num=9
print(type(num))#<class 'int'>
so=str(int)
print(type(so))#<class 'str'>

'''2.float--float()'''
num=9
print(type(num))#<class 'int'>
so=float(num)
print(type(so))#<class 'float'>

'''3.integer--int'''
nums=8.67
print(type(nums))#<class 'float'>
all_=str(nums)
print(all_)#8.67
print(type(all_))#<class 'str'>

'''string

1.integer--int()
float--float()
list
tuple
integer--int
#error we can't do str into int'''
how="i have 67 rupp"
print(type(how))#<class'str'>
who=int(how)
print(type(who))#error

how="67"
print(type(how))#<class 'str'>
who=int(how)
print(type(who))#<class 'int'>

'''2.float--float'''
how="6.86"
print(type(how))#<class 'str'>
who=float(how)
print(type(who))#<class 'float'>

'''3.list'''
how="2345"
print(type(how))#<class 'str'>
who=list(how)
print(type(who))#<class 'list'>

'''4.tuple--tuple()'''
how="2345"
print(type(how))#<class 'str'>
who=tuple(how)
print(type(who))#<class 'tuple'>


'''list
---
string--str()
tuple--tuple()

1.string--str()'''
nums=[1,2,3,4]
print(type(nums))#<class 'list'>
all_=str(nums)
print(type(all_))#<class 'str'>

'''2.tuple--tuple()'''
nums=[1,2,3,4]
print(type(nums))#<class 'list'>
all_=tuple(nums)
print(all_)#(1, 2, 3, 4)
print(type(all_))#<class 'str'>

      


'''tuple
-----
list
str

1.list'''
nums=(1,2,3,4)
print(type(nums))#<class 'tuple'>
all_=list(nums)
print(all_)#[1, 2, 3, 4]
print(type(all_))#<class 'list'>

'''2.str'''
nums=(1,2,3,4)
print(type(nums))#<class 'tuple'>
all_=str(nums)
print(all_)#(1, 2, 3, 4)
print(type(all_))#<class 'str'>
'''
-------------------------------------------------------------------------------------------------------------------------------------
concatination

--->(+)'''
num=8
num_2=9
print(num+num_2)#17

any_='python is a '
we='Language'
print(any_+we)#python is a Language

nums=[1,2,3]
all_=[3,4]
print(nums+all_)#[1, 2, 3, 3, 4]












