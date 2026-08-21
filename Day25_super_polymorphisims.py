'''
super() Method
--------------
-->this super() method is used to get the constructor from the
parent and use in the child class.
--> And also can get any method from the class.
'''
class person:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
        print('Person constructor called')
class employee(person):
    def __init__(self,name,age,role,salary):
        super().__init__(name,age,role)
        self.salary=salary
        print('Employee constructor called')
obj=employee('Durga',21,'Python Developer',25000)
print(obj.name)
print(obj.age)
print(obj.role)
print(obj.salary)



class all_:
    def job_(self):
        print('I am looking for job')
class looking(all_):
    def job_in(self):
        super().job_()
        print('looking for condidate')
    def an_(self):
        super().job_()
        print('No jobs')
any_=looking()
any_.an_()

'''
Polymorphism
------------
-->Polymorphism means a same name but different forms.
1.Method Overloading
2.Method Overriding
3.Operation Overloading

1.Method Overloading
-->This method overloading happens in class a method is
created with same name,but the recent method will be activated
and the before one will not the considered.
eg:
--
'''
class data:
    def add_(self,a,b):
        return a+b
    def add_(self,a,b,c):
        return a+b+c
    def add_(self,a,b,c,d):
        return a+b+c+d
    
obj=data()
print(obj.add_(2,3,4,5))

'''
2.Method Overriding
-->this method overriding happens when parent class and child class
same method  and the child class take its own implementation.
eg:
--
'''
class pay:
    def payment(self):
        print('payment called')
class UPI(pay):
    def payment(self):
        print('UPI payment called')

class paytm(pay):
    def payment(self):
        print('Paytm payment called')
obj=UPI()
obj.payment()

go=paytm()
go.payment()

'''
3.Operation Overloading
-->it gives special meaning to the operator when it called by object.
1.__add__:+
2.__sub__:-
3.__mul__:*
4.__truediv__:/

1.__add__:+'''
class cal:
    def __add__(self,a,b):
        print(a+b)
how=cal()
how.__add__(2,3)


class cal:
    def __init__(self,any_):
        self.any_=any_
    def __add__(self,do):
        print(self.any_+do.any_)
how=cal(78)
who=cal(64)
how.__add__(who)
print(how+who)

'''
2.__sub__:-'''
class cal:
    def __init__(self,any_):
        self.any_=any_
    def __sub__(self,do):
        print(self.any_-do.any_)
how=cal(78)
who=cal(64)
how.__sub__(who)
print(how-who)

'''
3.__mul__:*'''
class cal:
    def __init__(self,any_):
        self.any_=any_
    def __mul__(self,do):
        print(self.any_*do.any_)
how=cal(78)
who=cal(64)
how.__mul__(who)
print(how*who)
'''
4.__truediv__:/'''
class cal:
    def __init__(self,any_):
        self.any_=any_
    def __truediv__(self,do):
        print(self.any_/do.any_)
how=cal(78)
who=cal(64)
how.__truediv__(who)
print(how/who)

































