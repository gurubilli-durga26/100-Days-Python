'''output formatting
   -----------------
1.comma seperation:'''
name='Durga'
age=21
print('Welcome',name,'your age is',age)#Welcome Durga your age is 21


'''2.F-string(doc-string)'''

name='Durga'
age=21
print(f'Welcome {name} your age is {age}')

'''#%s-->all'''
name='durga'
age=45
print('name:%s'%name)#name:durga

'''#%d-->digits'''
price=89
print('name:%d'%price)#name:89
'''#%f-->float'''
price=89
print('name:%f'%price)#name:89.000000
3.dot format:


name='durga'
age=89
print('name:{}\nage:{}'.format(name,age))#/n is used to next line

'''#STATEMENTS
1.Condition
  1a.if
  2b.else
  3c.elif
  4d.nested if
2.Control
  1a.break
  2b.continue
  3c.pass
3.loop
  1a.while
  2b.for
'''
#if condition:if condition is used to check it is true or false

age=int(input('enter age:'))#18
if age>=18:
    print(f'your age is {age} and eligible to vote')#your age is 18 and eligible to vote

#if-else:else is the fall-back statement,incase if condition is false then this else block will execute .

age=int(input('enter age:'))#17
if age>=18:
    print(f'your age is {age} and eligible to vote')
else:
    print(f'your age is{age} ,you have to wait{18-age} years')#your age is17 ,you have to wait1 years
    
#even number or odd number
num=int(input('enter a num:'))#79
if num % 2==0:
    print(f'{num} is a even number')
else:
    print(f'{num} is a odd number')#79 is a odd number

#vowels or consonant

vol=input('enter letter:')#aui
if vol in'AEIOUaeiou':
    print(f'{vol} is vowel')
else:
    print(f'{vol} is consonant')#aui is consonant

#palindrome or not a palindrome

so=input('enter word:')
do=so[::-1]
print(do)
if so[::-1]==so:
    print(f'{so} is plaindrome')
else:
    print(f'{so} is not a plaindrome')

#leap year or not

year=int(input('enter year:'))
if year%4==0 and year%100!=0 or year%400==0:
         print(f'{year} is a leap')
else:
    print(f'{year} is not a leap')


#mobile number is indian number or not

mobile=input('enter mobile number:')
length=len(mobile)
if length==10:
           print(f'{mobile} is a indian mobile number')
else:
     print(f'{mobile} is not a indian mobile number')




