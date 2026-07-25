'''#table'''
tab=int(input('enter a num:'))
for j in range(1,11):
    print(f'{tab}x{j}={tab*j}')
'''
output:
enter a num:8
8x1=8
8x2=16
8x3=24
8x4=32
8x5=40
8x6=48
8x7=56
8x8=64
8x9=72
8x10=80
'''

'''#armstrong number'''
num=input('Enter num:')
length=len(str(num))
am=0
for i in str(num):
    am=int(i)**length+am
if am==int(num):
    print(f'{num} is Armstrong')
else:
    print(f'{num} is not a Armstrong')
'''
output:
Enter num:153
153 is Armstrong
'''

'''#febinocci number'''
limit=int(input('enter limit:'))
num=0
num_1=1
print(num,num_1,end=' ')
for i in range(1,limit+1):
    all_add=num+num_1
    num=num_1
    num_1=all_add
    print(all_add,end=' ')
'''
output:
enter limit:10
0 1 1 2 3 5 8 13 21 34 55 89 
'''
    
'''#calculator'''
num_1=int(input('Enter a num:'))
num_2=int(input('Enter a num:'))
op=int(input('enetr \n1.add \n2.sub \n3.multiple \n4.division \n5.power \n'))
if op==1:
    print(num_1+num_2)
elif op==2:
    print(num_1-num_2)
elif op==3:
    print(num_1*num_2)
elif op==4:
    print(num_1/num_2)
else:
    print(num_1**num_2)
'''
output:
Enter a num:10
Enter a num:2
enetr 
1.add 
2.sub 
3.multiple 
4.division 
5.power 
4
5.0
'''
