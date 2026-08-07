'''
Exception Handling
------------------
-->An error can be handled by try and except
1.try:
------
-->we can the check code here which  may contain any error.
eg:
--
'''
try:
    print(n)
except:
    print('some error')#some error
'''
2.except:
-->exception can handle any error that come in the try block
eg:
--
'''
try:
    num=0
    num_2=6
    print(num_2/num)
except:
    print('will get an error')#will get an error
'''
num=8
num_2=0
print(num/num_2)#ZeroDivisionError: division by zero

eg:
--
'''
try:
    any_=int(input('Enter any number:'))
    print(any_+9)
except:
    print('error')

#o/p:
'''
Enter any number:python
error


eg:
--
'''
try:
    print(9+'python')
except:
    print('error')#error

'''
3.else:
-------
-->if no error in the code were raised,then the else block will execute.
eg:
--
'''
try:
    print(9+5)
except:
    print('error')
else:
    print('no error')
#o/p:
'''
14
no error


eg:
--
'''
try:
    print(9/0)
except ZeroDivisionError:
    print('this will raise ZeroDivisionError ')
else:
    print('no error')
#this will raise ZeroDivisionError 
'''
eg:
--
'''
try:
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('this will raise ZeroDivisionError ')
except NameError:
    print('this will raise nameerror') 
else:
    print('no error')
#this will raise ZeroDivisionError 

'''
eg:
--
'''
try:
    print('python'+9)
    print(9/0)
    print(num)
except ZeroDivisionError:
    print('this will raise ZeroDivisionError ')
except NameError:
    print('this will raise nameerror')
except TypeError:
    print('this will raise typeerror')
    
else:
    print('no error')
#this will raise typeerror

'''
4.finally:
-->the finally block will  execute if error is present in the try block or not
eg:
--
'''
try:
    print('python')
except ZeroDivisionError:
    print('this will raise ZeroDivisionError ')
except NameError:
    print('this will raise nameerror')
except TypeError:
    print('this will raise typeerror')
    
else:
    print('no error')
finally:
    print('end')
#o/p:
'''
python
no error
end


File Handling
-------------
-->An file handler is an object used to connect with that particular file.
1.with(keyword)
2.open()
1.with(keyword):by using with keyword no need close the file,it will close it by itself
syntax:
by file name
------------
with open('file_name','mode')as name:
'''
with open('keyword.txt','r')as file:
    print(file.read())
'''
by file path
------------
with open(r'file_path','mode')as name:



2.open()
--------
-->by using this open() we have to close the file by using close()
eg:
--
'''
any_=open('keyword.txt','r')
print(any_.read())
any_.close()


'''
modes
-----
1.'r'-->read
the 'r' mode is used for function read(),readline() and readlines()
eg:
--
'''
with open('keyword.txt','r')as file:
    print(file.read())
'''    
2.'w'-->write
the 'w' mode is used for write() function
eg:
--
'''
with open('keyword.txt','r')as file:
    print(file.read())
'''   
3.'a'-->append
the 'a' mode is used for write() function and it will add the text at last position
eg:
--
'''
with open('keyword.txt','a')as file:
    file.write('\ngood evening!')
'''
4.'x'-->creating a file
eg:
--
'''
with open('key.txt','x')as file:
    file.write('good evening!')

'''
function
--------
1.write()
2.read()
-->the read() function will read the file chunk by chunk where we can specify the size
eg:
--
'''
with open('keyword.txt','r')as file:
    print(file.read(20))
'''
3.readline()
-->it will only read one line at a time
eg:
--
'''
with open('keyword.txt','r')as file:
    print(file.readline())
'''
4.readlines()
-->the readlines() will read whole file and wirtten it in a list,where each line is one index in the list.
eg:
--
'''
with open('keyword.txt','r')as file:
    print(file.readlines())

with open('keyword.txt','r')as file:
    print(file.readlines())

