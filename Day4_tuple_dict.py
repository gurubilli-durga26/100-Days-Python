'''TUPLE
   -----
1.Index():
Syntax:variable_name.index item()
--->tuple is collection different datatypes that are represented in() and seperated by ,
--->tuple is immutable'''
go=(1,'java',[3,4],('python',78))
print(go)#(1,'java',[3,4],('python',78))
print(go.index('java'))#1
print(go[2][1])#4

'''2.count():
syntax:variable_name.count(item)'''
go=(1,'java',[3,4],('python',78))
print(go.count('python'))#0 (tuple inside tuple it can't count)
print(go.count('java'))#1
print(go.count(('python',78)))#1


'''DICTIONARY
   ----------
--->dict is a key:value pair
--->keys are values seperated by:
--->dict is represented by{}
--->keys must be immutable datatypes

methods
-------
1.keys
2.values
3.items
4.update
5.clear
1.keys syntax:dict.keys()
--->duplicate keys are not allowed (it will be override with last occurance)'''
details={'name':'durga','AC':23456,'PAN':98765,'ANDHAR':3278,'PIN':1234}
print(details.keys())#dict_keys(['name', 'AC', 'PAN', 'ANDHAR', 'PIN'])

'''2.values syntax:dict.values()'''
details={'name':'durga','AC':23456,'PAN':98765,'ANDHAR':3278,'PIN':1234}
print(details.values())

'''3.items syntax:dict.items()'''
details={'name':'durga','AC':23456,'PAN':98765,'ANDHAR':3278,'PIN':1234}
print(details.items())#dict_items([('name', 'durga'), ('AC', 23456), ('PAN', 98765), ('ANDHAR', 3278), ('PIN', 1234)])

'''4.update syntax:dict.update()'''
details = {'name':'durga','AC':23456,'PAN':98765,'ANDHAR':3278,'PIN':1234}
details.update({'gender': 'male'})
details.update({'name':'gurubilli'})
print(details)#{'name': 'gurubilli', 'AC': 23456, 'PAN': 98765, 'ANDHAR': 3278, 'PIN': 1234, 'gender': 'male'}

'''5.clear():clear the entire dict
syntax:dict.clear'''
details = {'name':'durga','AC':23456,'PAN':98765,'ANDHAR':3278,'PIN':1234}
print(details.get('name'))#durga
details.clear()
print(details)#{}




