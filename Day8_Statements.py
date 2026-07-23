'''STATEMENTS'''
#elif
#grades for marks

marks=int(input('Enter your marks:'))
if marks>=90:
    print('A+')
elif marks>=80:
    print('A')
elif marks>=70:
    print('B+')
elif marks>=60:
    print('B')
elif marks>=50:
    print('C+')
elif marks>=40:
    print('c')
else:
    print('fail')

#find out greater value

num_1=int(input('enter number1:'))
num_2=int(input('enter number2:'))
num_3=int(input('enter number3:'))
if num_1>num_2 and num_1>num_3:
    print(f'{num_1} is greater value')
elif num_2>num_1 and num_2>num_3:
    print(f'{num_2} is greater value')
else:
    print(f'{num_3} is greater value')

#nested if
#checking ATM pin is correct or not

details={'ATM pin':'3456'}
atm=input('enter your 4 digit atm pin:')
if len(atm)==4:
    if atm==details['ATM pin']:
        op=int(input('enter \n1.withdraw \n2.deposit \n3.pinchange'))
        if op==1:
            money_withdraw=int(input('enter money:'))
        elif op==2:
            deposit=int(input('enter money to deposit:'))
    else:
        print('incorrect pin entered')
else:
    print('plz enter only 4 digit pin')

#control statement
#1.break:target is find it will break the loop
    
num=[34,67,90,107,45]
for i in num:
    if i==90:
        break
    print(i)
else:
    print('end')

#2.continue:skips the particular iteration
num=[34,67,90,107,45]
for i in num:
    if i==90:
        continue
    print(i)
else:
    print('end')
#pass:'''
'''-->space holder
-->if a statement is incomplete if we put pass after that no error will be raised'''
num=[24,36,78,45,90]
for i in num:
    pass
#loops
'''1.for loop
   2.while loop'''

#1.for loop:
'''-->for loop used to itterate over sequence such as str,list,tuple.
-->else in for loop it will execute when whole itterates are completed.
-->incase if condition becomes true,then else will never execute.'''
#range():function is used to generate number upto a limit.

#syntax---range(start,end,step)
'''ex:'''
for j in range(1,10,2):#(start,end,step)
    print(j)
'''ex:'''   
num='python is language'
for i in num:
    print(i)


#2.while loop

num=1
while num<10:
    print(num)
    num+=1

#assert keyword: the keyword is used to check the condition.
'''ex:'''
age=18
assert age>=18,'not eligible'
print('eligible')
'''ex:'''
marks=45
assert marks>=35,'fail'
print('pass')

    
