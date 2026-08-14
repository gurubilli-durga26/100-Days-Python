'''
OOPS
----
-->object oriented programming system
-->OOPs is used to maintain the code structure in object and classes.

1.class
2.object
3.attribute
4.methods

1.class:
-------
-->class is an buleprint or template to an object.
syntax:
------
class(Keyword) Name:
    #attribute
    #methods

2.object:
-->object is instance of the class.
syntax:
------
class(Keyword) Name:
    #attribute
    #methods
any_=class_name
#eg:
class person:
    name='Durga'
    edu='B.Tech'
p1=person()
print(p1.name)
print(p1.edu)
#O/P:
Durga
B.Tech
#eg:
class codegnan:
    city='HYD'
    tech='Python'
    data='MySQL'
code=codegnan()
print(code.city)
#O/P:HYD

3.Attributes
------------
-->Attribute is the data present in the class or pass to the class.
eg:
--
take car
--------
color
seat
brand
#eg:
class car:
    def __init__(self):
        self.color='Red'
        self.seat=6
        self.brand='BMW'
c1=car()
print(c1.color)
print(c1.seat)
print(c1.brand)
#O/P:
Red
6
BMW
#eg:
class details:
    def __init__(self):
        self.name='Durga'
        self.age=21
        self.Back_G='B.Tech'
        self.role='Student'
person=details()
print(person.name)
print(person.age)
print(person.Back_G)
print(person.role)
#O/P:
Durga
21
B.Tech
Student

#eg:
class bank_details:
    def __init__(self):
        self.name='Durga'
        self.aadhaar=7256568663
        self.pan='ffg345jfkh'
        self.phone_no=987652538
person=bank_details()
print(person.name)
print(person.aadhaar)
print(person.pan)
print(person.phone_no)
#O/P:
Durga
7256568663
ffg345jfkh
987652538


4.Methods:
---------
-->Method is a function that is created inside the class.
syntax:
------
class(keyword) name:
    #attributes
    def fun_name(self):
        #code
obj=class_name()
print(obj.fun_name())
#eg:
class student:
    def __init__(self):
        self.name='Durga'
        self.age=21
        self.course='PFS'
    def st_name(self):
        print(self.name)
        print(self.age)
        print(self.course)
    def all_data(self):
        print(self.name)
        print(self.age)
stu=student()
stu.st_name()
stu.all_data()
#O/P:
Durga
21
PFS
Durga
21

#eg:
class car:
    def __init__(self):
        self.color='Red'
        self.seat=6
        self.brand='BMW'
    def brake(self):
        print(f'{self.brand} brake will apply at speed 250KM')
    def accelator(self):
        print(f'{self.brand} will take 2 sec to reach 180 speed')
    def clucth(self):
        print(f'{self.brand} with {self.seat} is automatic')

c1=car()
c1.brake()
c1.accelator()
c1.clucth()
#O/P:
BMW brake will apply at speed 250KM
BMW will take 2 sec to reach 180 speed
BMW with 6 is automatic

#eg:   
class students:
    def __init__(self,name,age,batch):
        self.name=name
        self.age=age
        self.batch=batch
    def all_data(self):
        print(self.name)
        print(self.age)
        print(self.batch)
stu_1=students('Durga',21,5)
stu_1.all_data()

stu_2=students('usha',21,5)
stu_2.all_data()
#O/P:
Durga
21
5
usha
21
5
'''
#eg:
class bank:
    def __init__(self,name,aadhaar,pan,phoneno):
        self.name=name
        self.aadhaar=aadhaar
        self.pan=pan
        self.phoneno=phoneno
    def all_data(self):
        print(self.name)
        print(self.aadhaar)
        print(self.pan)
        print(self.phoneno)
details_1=bank('Durga',2465446765,'reds56yhyg',45678909834)
details_1.all_data()
























