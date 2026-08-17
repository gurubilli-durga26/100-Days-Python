'''
Constructer
-----------
-->__init__
-->The constructor is a special method that only run when the object is created.
-->Mostly we will take data inside this method.
ex:
--
'''
class cls_data:
    def __init__(self):
        self.name='Durga'
        self.course='Python'
cls=cls_data()
print(cls.name)
print(cls.course)
#o/p:
'''
Durga
Python

self
----
-->the self keyword reffers to current object.'''
class stu:
    def __init__(self):
        self.name='Durga'
    def any_(self):
        print(self.name)
s1=stu()
s1.any_()

class stu_data:
    def __init__(self,name,batch,age):
        self.name='Durga'
        self.batch=batch
        self.age=age
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')
data1=stu_data('Durga',5,21)
data1.student()
#o/p:
'''
Durga
Durga from batch 5 and age 21


Encapsulation
-------------
-->wrapping data and methods together is called as encapsulation and using or controlling the data in methods.'''
class stu_data:
    def __init__(self,name,batch,age):
        self.name='Durga'
        self.batch=batch
        self.age=age
    def student(self):
        print(f'{self.name} from batch {self.batch} and age {self.age}')
data1=stu_data('Durga',5,21)
data1.student()
#o/p:
'''
Durga from batch 5 and age 21

Access Specifiers
-----------------
1.public    (name)
-->this  can be access normally and can call it like a normal variable.
eg:
--
self.name=name
print(self.name)

2.proctected(_name)
-->Just adding single(_) before a variable it becomes proctected variable.
eg:
--
self._age=age
print(self._age)
'''
class stu_data:
    def __init__(self,name,batch,age,fee):
        self._name='Durga'
        self._batch=batch
        self._age=age
        self._fee=fee
    def only_name(self):
        print(f'{self._name}')
    def only_batch(self):
        print(f'{self._batch}')
    def only_age(self):
        print(f'{self._age}')
    def only_fee(self):
        print(f'{self._fee}')
    
data1=stu_data('Durga',5,21,45000)
data1.only_name()
data1.only_batch()
data1.only_age()
data1.only_fee()
#o/p:
'''
Durga
5
21
45000


3.private   (__name)
-->Adding (__) before a variable it becomes private
ex:
--
self.__balance=balance
print(self.__balance)
'''
class bank_ac:
    def __init__(self):
        self.name='Teja'
        self.Adr=123456789
        self.Pan='asde455rttgd'
        self.__balance=45000
    def details(self):
        print(self.name)
        print(self.Adr)
        print(self.Pan)
    def bal(self):
        print(self.__balance)

ac=bank_ac()
ac.details()
ac.bal()
#o/p:
'''
Teja
123456789
asde455rttgd
45000
'''
      
class employee:
    def __init__(self):
        self.name='Durga'
        self.role='Python Developer'
        self.__salary=82000
        self._experience=4.5
        self._emptype='full-time'
    def details(self):
        print(self.name)
        print(self.role)
    def income_(self):
        print(self.__salary)
    def type_(self):
        print(self._experience)
        print(self._emptype)
emp=employee()
emp.details()
emp.income_()
emp.type_()
#o/p:
'''
Durga
Python Developer
82000
4.5
full-time
'''

class university:
    def __init__(self):
        self.name='Durga'
        self.branch='ECE'
        self.section='A'
        self.reg_no=22453
        self.fee=45000
    def details(self):
        print(self.name)
        print(self.branch)
    def roll_no(self):
        print(self.reg_no)
    def amount(self):
        print(self.fee)

u1=university()
u1.details()
u1.roll_no()
u1.amount()
#o/p:
'''
Durga
ECE
22453
45000
'''
























