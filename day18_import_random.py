'''
import random
-------------
'''
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

'''
ascii_letters-->this string module function that can give
upper and lower letters'''

import string
print(string.ascii_letters)

'''digits-->string module function that can give number(0-9)'''

import string
print(string.digits)

'''punctuation-->this string module function can give us punctuation'''

import string
print(string.punctuation)

#password generator
import random
import string
letters=string.ascii_letters
digits=string.digits
punctuation=string.punctuation
special_char='@#$*'
all_chars=letters+digits+punctuation+special_char
password=''
for i in range(5):
    password+=random.choice(all_chars)
print(password)

#printing data and time in ATM program
bank_balance=10000
from datetime import datetime
import sys
now=datetime.now()

while True:
    print('----welcome to SBI ATM----')
    user_opt=int(input('\n1.withdraw \n2.deposit \n3.check balance \n4.exit'))
    if user_opt==1:
       with_m=int(input('enter the money you want to withdraw:'))
       if with_m<=bank_balance:
          bank_balance-=with_m
          print(f"remaining money:{bank_balance} {now.strftime('%H:%M %y-%m-%d')}")
       else:
           print('insufficient money')
    elif user_opt==2:
        deposit_m=int(input('enter the money you want to deposit:'))
        bank_balance+=deposit_m
        print(f"money added succesfully:{bank_balance} {now.strftime('%H:%M %y-%m-%d')}")
    elif user_opt==3:
        print(f"avaliable balance:{bank_balance} {now.strftime('%H:%M %y-%m-%d')}")
    elif user_opt==4:
        sys.exit()
    else:
        print('incorrect chioce')
        print('Thank for visiting the ATM')
        sys.exit()

#guess the number        
import random
num=random.randint(1,100)
user_opt=int(input('pick a number(1-100):'))
if user_opt==num:
    print(f'you have picked{user_opt} number')
else:
    print(f'better luck next time')                      
