'''#Generate even and odd upto certain numbers

limit=int(input('Enter the limit:'))
for j in range(1,limit+1):
    if j%2==0:
        print(f'{j} is a even')
    else:
        print(f'{j} is a odd')
output:
Enter the limit:10
1 is a odd
2 is a even
3 is a odd
4 is a even
5 is a odd
6 is a even
7 is a odd
8 is a even
9 is a odd
10 is a even


#Generate prime or not upto certain numbers
num=int(input('Enter number:'))
count=0
for j in range(1,num+1):
    if num%j==0:
        count+=1
if count==2:
    print(f'{num}is a prime')
else:
    print(f'{num}is not a prime')
output:
Enter number:7
7is a prime

#By using Internal for loop to generate prime or not
for i in range(2,10):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(f'{i} is a prime')
    else:
        print(f'{i} is not a prime')
output:
2 is a prime
3 is a prime
4 is not a prime
5 is a prime
6 is not a prime
7 is a prime
8 is not a prime
9 is not a prime

#string reverse and checking plaindrome or not
word=input('Enter a word:')
empty=''
for j in word:
    empty=j+empty
if empty==word:
    print(f'{word} is a plaindrome')
else:
    print(f'{word} is not a palindrome')
output:
Enter a word:madam
madam is a plaindrome

#print right triangle star
start=int(input('enter a num:'))
for j in range(1,start+1):
    for i in range(1,j+1):
        print('*',end='')
    print()
output:
enter a num:4
*
**
***
****
  
#print right triangle numbers
start=int(input('enter a num:'))
for j in range(1,start+1):
    for i in range(1,j+1):
        print(i,end='')
    print()
output:
enter a num:4
1
12
123
1234
#increment right triangle numbers
count=0
start=int(input('enter a num:'))
for j in range(1,start+1):
    for i in range(1,j+1):
        count+=1
        print(count,end='')
    print()
output:
enter a num:4
1
23
456
78910

#reverse right angle triangle star

count=0
start=int(input('enter a num:'))
for j in range(start,0,-1):
    for i in range(1,j+1):
        count+=1
        print('*',end='')
    print()
output:
enter a num:4
****
***
**
*

#

count=0
start=int(input('enter a num:'))
for j in range(start,0,-1):
    for i in range(1,j+1):
        count+=1
        print(count,end='')
    print()
output:
enter a num:4
1234
567
89
10

#
'''
start=int(input('enter a num:'))
for j in range(start,0,-1):
    for i in range(1,j+1):
        print(i,end='')
    print()
'''
#triangle star
num=7
for j in range(num):
    print(' '*(num-j-1),end='')
    print('* '*(j+1))
output:
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * * 

#reverse triangle star
num=7
for j in range(num,0,-1):
    print(' '*(num-j),end='')
    print('* '*(j))
output:
* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 

#Duplicate values
nums=[1,2,2,5,5]
empty=[]
for j in nums:
    if j not in empty:
        empty.append(j)
print(empty)
output:
[1, 2, 5]

#perfect number
num=int(input('Enter a num:'))
perfect_num=0
for j in range(1,num):
    if num%j==0:
        perfect_num+=j
if perfect_num==num:
    print(f'{num} is perfect number')
else:
    print(f'{num} is perfect number')
output:
Enter a num:6
6 is perfect number
'''
