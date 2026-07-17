'''to find datatype -- type(variable_name)
   to find memory -- id(variable_name)
--------->Datatypes<---------------------------
int:
num=9

float:decimal values
num=89.45
`11`string:sequence of char that are inclosed in('','' '', '''  ''')
       str immutable'''

so='python is a language'
for j in so:
    print(j)

'''str Methods:
1.replace():used to replace old str with new str'''
so='python is a  language'
print(so.replace('python','java'))
print(so)

'''syntax----variable_name.replace('old_str,'new_str','how many')
program:'''
so='python is a  language python python'
print(so.replace('python','java'))
print(so.replace('python','java',2))
      
'''2.join():this method will add the new char after every sub-string
syntax---'new-string'.join(variable_name)'''
so='python is a  language'
print('-'.join(so))


'''3.split():'''
so='python is a language'
print(so.split('is'))


'''4.index():it represent position value'''
so='python is a language'
print(so.index('s'))

'''5.count():'''
so='python is a language'
print(so.count('n',10,16))


so='python is a language'
print(so[13])#index




'''list():list is a collection of different datatypes(str,int...etc) that are represented in [] and separated by ,
       mutable datatype:can do modification on variable.'''
any_=[1,'python',[2,['python',9],4],'java',['python',[56,78],'java',90]]
print(any_[4])
'''list methods:
1.append():this method is used to add new item into the list and it will add at last index position.'''
any_=[1,2,3,4,5]
any_.append("python")
print(any_)

'''2.Extend():'''
any_=[1,2,3,4,5]
any_.append("python")
print(any_)
any_.extend("python")
print(any_)


'''3.remove():remove will delete the item based on the value given
          if the value not in the list will throw the error'''

any_=[1,2,3,4,5]
any_.remove(2)
print(any_)

'''4.pop():remove will delete the item based on the index position given
        if the index position is out of the range in the list will throw the error.'''
any_=[1,2,3,4,5]
any_.pop(2)
print(any_)

    







