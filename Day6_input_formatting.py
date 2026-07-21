'''input formatting
   ----------------
1.int:int(input())'''

num=int(input('enter a num:'))#6
print(num+9)#15
print(type(num))#<class 'int'>

'''2.string:input()'''

we=input('enter:')#6 (integers given also it will take as str)
print(type(we))#<class 'str'>

'''3.list:'''

num=list(map(int,input('enter nums:').split()))#45 65 7
print(num)#[45, 65, 7]

num=input('enter num:').split()#45 65 7
print(num)#['45', '65', '7']

'''4.tuple:'''

nums=tuple(map(int,input('enter nums:').split()))#45 65 7
print(nums)#(45, 65, 7)

nums=eval(input('enter:'))#'python'#78
print(type(nums))#<class 'str'>#<class 'int'>


'''python-->reverse(nohtyp)'''

num='python'
print(num[::-1])#nohtyp

'''#24h-12h clock'''

time=input('enter 24H clock:')#21:23
parts=time.split(':')
hours=int(parts[0])-12
print(hours,':',parts[1],'pm')#9 : 23 pm

          


