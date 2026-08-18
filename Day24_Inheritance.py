'''
Inheritance
-----------
-->Inheritance is the process of inherite one class into another class.
-->will generally inherite from a class is called parent class
and usinf it in another class is called child class.
eg:
--
'''
class company:
    def salary(self):
        print('Company salary')
class employee(company):
    def mon_sal(self):
        print('Employee salary')
per_sal=employee()
per_sal.mon_sal()
per_sal.salary()

'''
TYPES:
-----
1.single inheritance
2.multiple inheritance
3.multi-level inheritance
4.hierarchical inheritance
5.hybrid inheritance

1.Single Inheritance:
-->if one class is inherite from one parent class.
This is known as Single Inheritance.
eg:
--
'''
class father:
    def land(self):
        print('5 acer land')
class me(father):
    def flat(self):
        print('6 flat')
all_=me()
all_.flat()
all_.land()
'''
2.Multiple Inheritance:
-->if one child inherite from more than one parent class.
this is called Multiple Inheritance.
eg:
--
'''
class father:
    def home(self):
        print('Home at Village')
class mother:
    def gold(self):
        print('50KG gold')
class son(father,mother):
    def flat(self):
        print('sons flat')
all_to=son()
all_to.home()
all_to.gold()
all_to.flat()
'''
3.Multi-Level Inheritance:
-->One child class become parent class to the another is called
multi-level inheritance
eg:
---
'''
class grandfather:
    def land(self):
        print('Grandfather Land')
class father(grandfather):
    def flat(self):
        print('Father Flat')
class son(father):
    def car(self):
        print('Sons Car')

fam=son()
fam.land()
fam.flat()
fam.car()

'''
4.Hierarchical Inheritance:
-->If two child classes inherite from one parent is called
hierarchical inheritance.
eg:
--
'''
class father:
    def land(self):
        print('50 acer land')
class son_1(father):
    def flat(self):
        print('first son flat')
class son_2(father):
    def car(self):
        print('second son car')

s1=son_1()
s1.land()
s1.flat()

s2=son_2()
s2.land()
s2.car()
'''
5.Hybrid Inheritance:
-->Inherite from more than two types into one in one class is called as
Hybrid Inheritance.
eg:
--
'''
class person:
    def name(self):
        print('Durga is his name')
class student(person):
    def study(self):
        print('B.Tech final year')
class py_teacher:
    def teach(self):
        print('Python')
class java_teacher:
    def teac(self):
        print('Java')
class learner(py_teacher,java_teacher):
    def learn(self):
        print('Learner')
class all_get(student,learner):
    def get_it(self):
        print('this person getting all the data')
all=all_get()
all.name()
all.study()
all.teach()
all.teac()
all.learn()
all.all_get()


#single 
class student:
    def name(self):
        print('Durga')
class branch(student):
    def depart(self):
        print('ECE')
data=branch()
data.name()
data.depart()

#multiple 

class learn:
    def institute(self):
        print('Codegnan')
class pfs:
    def py(self):
        print('Taken pfs course')
class trainee(pfs,learn):
    def name(self):
        print('Durga')

stu=trainee()
stu.institute()
stu.py()
stu.name()


#multi-level

class learn:
    def institute(self):
        print('Codegnan')
class pfs(learn):
    def py(self):
        print('Taken pfs course')
class trainee(pfs):
    def name(self):
        print('Durga')

stu=trainee()
stu.institute()
stu.py()
stu.name()

'''
#hierarchical inheritance
class university:
    def collage(self):
        print('vignan')
class stu_1(university):
    def name(self):
        print('Durga')
class stu_2(university):
    def stu2_name(self):
        print('Meghana')
s1=stu_1()
s1.collage()
s1.name()

s2=stu_2()
s2.collage()
s2.stu2_name()



















