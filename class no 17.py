### Class variable(static variable) and Instance Variables
  ## - class varaibles and static variables are same
class Car:
    # static or class level variable
    # can be updated using class name for all objects
    wheels = 4
    
    def __init__(self):
    # non static or object/instance level variable
    # can be updated using object name for a particular object
        self.mileage = 10
        self.company = "BMW"
c1 = Car()
c2 = Car()
# since wheel is a class level variable can be accessed using class name
print(Car.wheels)
print(c1.wheels)

print(c1.mileage)
# print(Car.mileage)
Car.wheels = 5
print(Car.wheels)

print(c1.wheels)
class ABC():
    name ="Waqas" 
abc = ABC()
abc.name = "Kashif"
c1.wheels = 100
# class level variable is updeated using class, will be udated for every object
Car.wheels = 20
Car.wheels, c1.wheels,c2.wheels
## Class methods , Instance methods , static methods
 - Class methods and startic methods are not same
class Student:
    school = "SSUET"
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance methods
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    # instance methods
    def information(self):
        return self.school
s1 = Student(89,98,90)
s2 = Student(80,90,70)

# instance method called using instance  s1
print(s1.avg())

# instance method called using instance  s2
print(s2.avg())

# instance method called using class name but instance is passed a argument
print(Student.information(s1))
print(Student.information(s2))
print(Student.school)
print(s1.school)

# instance method called using class name>>error
print(Student.information())
print(Student.avg())
avg is an instance method it required a instance/object to be called.
information is a also a instance method which requires instance/object to be called.

any instance method can not be called using a class name.

we need a class method to be called by using a class name

class methods can be called using class name as well as instance name
to make a methods class method we use a decorator @classmethod
this way information method can be called using an object as well as a class
class Student:
    # class variable
    school = "SSUET"
    def __init__(self, m1,m2,m3):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    # instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod # decorator
    def information(cls):
        return cls.school
s1 = Student(89,98,90)
s2 = Student(80,90,70)
# instance method called using instance  s1
print(s1.avg())
# instance method called using instance  s2
print(s2.avg())

########Class method can be called using class as well as instance######

# class method is called using instance
print(s1.information())
print(s2.information())

# class method is called using class name
print(Student.information())
print(Student.information())
# Static Methods
 - static methods are methods that donot require instance or class
class Student:
    school = "SSUET"
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def information(c):
        return c.school

    @staticmethod
    def hello():
        return "Im a static method"
s4 = Student(23,24,25)
print(s4.hello())
s4.avg()
Student.hello()
class Battery():
    def __init__(self,manuf, cell, weight, amp, watt,price):
        self.manuf =manuf
        self.cell =cell
        self.weight=weight
        self.amp =amp
        self.watt =watt
        self.price =price
class ElecCar:
    def __init__(self,make,model,year,engine):
        self.make =make
        self.model = model
        self.year = year
        self.engine =engine
        # instance used as attributes
        self.battery = Battery("Osaka",27,60,200,12,60000)
    def carruns(self):
        pass
    def carstop(self):
        pass

e = ElecCar('honda',2024,2024,2000)
e.battery.price
# Inner Classes
 - Class inside a class is called inner class
class Student:
    def __init__(self, name, rollno):
        self.name =name
        self.rollno=rollno
    def show(self):
        print(self.name, self.rollno)
s1 = Student('Nasir',2)
s2 = Student('Hassan',3)

s1.show()
s2.show()
Case: A student in IT class must hava laptop
so there is an attribute of laptop for student
class Student:
    def __init__(self, name, rollno,laptop):
        self.name =name
        self.rollno=rollno
        self.laptop = laptop
    def show(self):
        print(self.name, self.rollno,self.laptop)
s1 = Student('Nasir',2, "HP")
s2 = Student('Hassan',3,"Lenovo")

s1.show()
s2.show()
What if i need to add more detail of my laptop??

Should i send the details as arguments to init??

We can create a separate class for laptop and use its object as attribute to Student

or we can also create an inner class of laptop inside Student
### Instance as attribute
A class outside the class, its instance can be used as attribute in another class
class Laptop:
    def __init__(self,brand,cpu,ram):
        self.brand =brand
        self.cpu =cpu
        self.ram =ram

    def show(self):
        print(self.brand,self.cpu,self.ram)
class Student:
    def __init__(self, name, rollno):
        self.name =name
        self.rollno=rollno
        self.laptop = Laptop("Hp","Corei7",16)

    def show(self):
        print(self.name, self.rollno)
        self.laptop.show()


s1 = Student('Nasir',2,)
s2 = Student('Hassan',3,)

s1.show()

s2.show()

### Inner Class
 - A class clreated inside a class is called inner class
class Student:
    def __init__(self, name, rollno):
        self.name =name
        self.rollno=rollno
        self.laptop = self.Laptop("Hp","i7",'16Gb')

    def show(self):
        print(self.name, self.rollno)
        self.laptop.show()

    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand =brand
            self.cpu =cpu
            self.ram =ram
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student('Nasir',2)
s2 = Student('Hassan',3)

s1.show()

s2.show()
s1.laptop.show()
s2.laptop.show()
# Inheritance
class A:
    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("Feature2 is working")


a1 = A()
a1.feature1()
a1.feature2()
### Single inheritance
class B(A):
    def feature3(self):
        print("Feature3 is working")
    def feature4(self):
        print("Feature4 is working")
b1 = B()
b1.feature1()
b1.feature3()
b1.feature4()
b1.feature2()
#### Multilevel Inheritance
class C(B):
    def feature5(self):
        print("Feature5 is working")
    def feature6(self):
        print("Feature6 is working")
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()
## Multiple Inheritance
class A:
    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("Feature2 is working")


a1 = A()
a1.feature1()
a1.feature2()
class B():
    def feature3(self):
        print("Feature3 is working")
    def feature4(self):
        print("Feature4 is working")
b1 = B()
b1.feature3()
b1.feature4()

class C(A,B):
    def feature5(self):
        print("Feature5 is working")
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
## Contructor in Inheritance and Method Resolution Order
class A:
    def __init__(self):
        print("In init of A")

    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("Feature2 is working")

class B(A):

    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")
a1=A()
b1=B()

# constructor of A will be called even if we are creating
# object of B since B dont have any contrcutor
class A:

    def __init__(self):
        print("In init of A")

    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("Feature2 is working")

class B(A):
    def __init__(self):
        print("In init of B")


    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")
a1=A()
b1=B()

# constructor of B will be called now as object of B is created
class A:

    def __init__(self):
        print("In init of A")

    def feature1(self):
        print("Feature1 is working")
    def feature2(self):
        print("Feature2 is working")

class B(A):
    def __init__(self):
        print("In init of B")
        super().__init__()

    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")
a1=A()
b1=B()

# if we want to call the init of A when object of B
#is creating we will use super()
class A:
    def __init__(self):
        print("In init of A")

    def feature1(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is working")
    def show(self):
        print("I am showing class A")
class B:
    def __init__(self):
        print("in init of B")


    def feature3(self):
        print("Feature3 is working")

    def feature4(self):
        print("Feature4 is working")

    def show(self):
        print("I am showing class B")
class C(A,B):
    def __init__(self):
        print("init of C")
        super().__init__()
        # now we have two parent classes super will call init of???
        # There is a term called MRO
        # Method resolution is from Left to Right
        # init of A will be called
c  = C()
# show() of class A will be called (MRO)
c.show()
class C(B,A):
    def __init__(self):
        print("init of C")
        super().__init__()
        # now we have two parent classes super will call init of???
        # There is a term called MRO
        # Method resolution is from Left to Right
        # init of A will be called
c  = C()
# show() of class B will be called (MRO)
c.show()
class A:
    def __init__(self):
        print("In init of A")

    def feature1(self):
        print("Feature1 is working")

    def feature2(self):
        print("Feature2 is A working")
    def show(self):
        print("I am showing class A")



class B():
    def __init__(self):
        print("in init of B")


    def feature2(self):
        print("Feature2 B is working")

    def feature4(self):
        print("Feature4 is working")

    def show(self):
        print("I am showing class B")


class C(A,B):
    def __init__(self):
        print("init of C")
        super().__init__()
        super().show()
    def feature2(self):
        print("I m in C")

    def feat(self):

        super().feature2()
c  = C()
c.feat()
# Polymorphism
  can be implemented by the following techniques:
 - Duck typing
 - Operator overloading
 - Method Overloading
 - Method Overriding

#### Duck Typing
If there a bird which is:
    - walking like a duck
    - which is quaking like a duck
    - which is swimming like a duck
          then it is a duck
          
Means its behaviour is just like a duck although it not a duck
class Student:
    def useLibrary(self):
        print("Reading Books")
        print("Making Notes")

s1 = Student()
################################
class Teacher:
    def useLibrary(self):
        print("Reading Books")
        print("Making Notes")
        print("Prepare Question Paper")

t1 = Teacher()
#####################################

class Library:
    def welcome(self, obj):
        obj.useLibrary()


lib  =Library()

lib.welcome(s1)
lib.welcome(t1)
#### Another Example of Duck Typing
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")
ide1 = PyCharm()

#################


class VsCode:
    def execute(self):
        print("Grammar Checking")
        print("Spell checking")
        print("Compiling")
        print("Running")
ide2 = VsCode()
#############################

class Laptop:
    def code(self,ide):
        ide.execute()

lap1 = Laptop()
lap1.code(ide1)
lap1.code(ide2)

# it matters not what class is but it must have a method execute
# like if it has a behaviour like a duck than it is a duck
### Operator Overloading
a = "hello"
class Merainteger:
    pass
mera_int1 = Merainteger()
print(type(mera_int1))
print(type(a))
print(mera_int1)
print(a)

a = 10
b = 20

print(a + b)
# when we use a + operator, in backend it calls add method of int class(that sums)
# because both the supplied operands are of type(class) integers \
# or we can say that both are objects of int class
print(int.__add__(a,b))
int.__add__(10,40)
help(int)
a = "10"
b = "20 "

print(a + b)
# when we use a + operator, in backend it calls add method of str class(that concatenates)
# because both the supplied operands are of type(class) string
# or we can say that both are objects of string class
print(str.__add__(a,b))
help(str)
class Student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2
s1 = Student(80,90)
s2 = Student(70,90)
# Can we add objects of Student class ?????
s1 + s2
#Since we have not defined any add function in student class that can add s1 and s2
# We will over load add method in our student class also
class Student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        return Student(m1,m2)


    def __gt__(self,other):
        sum_s1 = other.m1 + other.m2
        sum_s2 = self.m1 + self.m2
        if sum_s1 > sum_s2:return True
        else:return False


s1 = Student(80,90)
s2 = Student(70,60)
s3 = s1 + s2
print(s3)
# it will print the address of the object
# if we want to print the value
# we need to override a function __str__
s2>s1
s1>s2
a= 100
print(a)
help(str)
class Student:
    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        newObj = Student(m1,m2)
        return newObj

    def __str__(self):
        return f" Hello I am a student: {self.m1} {self.m2}"


    def __gt__(self,other):
        sum_s1 = other.m1 + other.m2
        sum_s2 = self.m1 + self.m2
        if sum_s1 > sum_s2:return True
        else:return False


s1 = Student(80,90)
s2 = Student(70,60)
s4 = s1 + s2
print(s4)
print(s1)
print(s2)
class Student:
    def __init__(self, m):
        self.m = m

    def __add__(self,other):
        new_m = self.m + other.m
        #130       60      70

        newObj = Student(new_m)#130
        return newObj

    def __str__(self):
        return f"{self.m}"


    def __gt__(self,other):
        other = other.m
        self = self.m
        if self > other:return True
        else:return False


s1 = Student(60)
s2 = Student(70)
print(s1)
print(s2)
s3 = s1+s2
print(s3)
print(s1>s2)
print(s2>s1)
# Abstraction
#### Abstract Class and Methods in Python
 - Python does not support Abstraction
 - we will use a module ABC for abstraction
 - ABC means Abstract Base Classes
# A normal class and a normal method
class Computer:
    def process(self):
        print('running')

# A method that only has declaration but has nothing in it is method
class Computer:
    def process(self):
        pass
# A class having a methods that has no body
Hiding the implementation details of a method is called abstraction
We can not create an object of abstract classes
com1 = Computer()
com1.process()

# There is no error and we are able to create onject and call method
# because its not an abstract class and not an abstract method.
from abc import ABC , abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def greet(self):
        print("Hello")
#        To make a class abstract
#           - It must inherit the ABC class from abc module
#           - It must have atleast a abstract method (which is defined using a decorator @abstractmethod)

com1 = Computer()

# We can not create the objects of abstract classes
class Laptop(Computer):

    def process(self):
        print("It is running")
#     def greet(self):
#         print("Salam")
lap1 = Laptop()
If we want to instantiate a drive class we must have to supply the implememtation of all the abstract methods of the abstract class.
#### What is the use this concept or functionality
Through abstraction we can provide a user an interface that only show the behaviour not the implmetation of that behaviour
Like we show a user a computer that runs process and user can only see the name of behavoiur but there is no implementation in it.
Implementation is done in child class
from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")
class Duster(Car):
     def mileage(self):
        print("The mileage is 24kmph ")
class Renault(Car):
    def mileage(self):
            print("The mileage is 27kmph ")
# Driver code
t= Tesla ()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()
# Python program to define
# abstract class

from abc import ABC
class Polygon(ABC):
    # abstract method
    def sides(self):
        pass

class Triangle(Polygon):
    def sides(self):print("Triangle has 3 sides")
class Pentagon(Polygon):
    def sides(self):print("Pentagon has 5 sides")
class Hexagon(Polygon):
    def sides(self):print("Hexagon has 6 sides")
class square(Polygon):
    def sides(self):print("I have 4 sides")
# Driver code
t = Triangle()
t.sides()

s = square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
k.sides()
# Python OOPs Public, Protected and Private
Public private and protected functionalities are highly restricted (strongly typed) in most of the typed languages
But in python you will not be restricted to access public private and protected variables, they can be overridden.
# All class ariables are public by defualt
# All instance variables are public by default
class Car():
    # public class variable can be accessed from any where
    wheels = 4
    def __init__(self,windows, doors, enginetype):

        #Public instance Variable can be acceesed from anywhere
        self.windows =windows
        self.doors =doors
        self.enginetype =enginetype
audi = Car(4,5,"Diesel")

# you can view the dir of audi object to check the aceessible item to it
# you will notice all three instance vairbbles are present in the list
dir(audi)
class Suzuki(Car):
    def __init__(self,windows,doors,enginetype, hp):
        super().__init__(windows,doors,enginetype)
        self.hp = hp
suz = Suzuki(4,4,"Petrol","1600")

# you will notice public variables are all accessible to child class also
dir(suz)
#### Proof of concept
#public variable can be accessed

print(audi.windows)

# public variable can be modified
audi.windows= 6
# accessing modified value
print(audi.windows)
# to make a variable protected use a single underscore before a variable name like _name = "Asad"
class Car():
    def __init__(self,windows, doors, enginetype):

        #Protected variables: should be acceesed from a sub class only by definition but python has no restriction it can also be accessed from any where
        # but python dont restrict actually
        self._windows =windows
        self._doors =doors
        self._enginetype =enginetype
        self.hello = "heooooooo"


audi = Car(4,5,"Diesel")
dir(audi)

class Suzuki(Car):
    def __init__(self,windows,doors,enginetype, hp):
        super().__init__(windows,doors,enginetype)
        self.hp = hp
suz = Suzuki(4,4,"Petrol","1600")

dir(suz)
audi.hello
audi.
audi._windows = 10
audi._windows
class Car():
    def __init__(self,windows, doors, enginetype):

        #Private Variable can not be acceesed from anywhere
        self.__windows =windows
        self.__doors =doors
        self.__enginetype =enginetype
#         self.name = "Nasir"
audi = Car(4,5,"Diesel")