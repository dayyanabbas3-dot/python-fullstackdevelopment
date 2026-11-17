# for i in range(10):
#   print("python")

# i=1
# while i<=5:
#     print("hello world") 
#     i+=1

# def greet():
#     print("hello students")
#     print("welcome to python")
# greet()  

# def add(a,b,c):
#     result=a+b+c
#     print(result)
# add(10,20,30)
# add(10,30,20)

# students=["syed","abbas","nibba","nibbi"]
# students.append("zafir")
# students.remove("abbas")
# students.insert(1,"nibba")
# print(students)

# student_details = ("syed",23,88,True)
# print(student_details[0])

# student={
#     "name":"syed",
#     "age":21,
#     "marks":87,
#     "passed":True,
#     "usn":"1gd24ci047"
# }
# student["course"]="python programing"
# student["marks"]=89
# print(student["name"])
# print(student["usn"])
# print(student["marks"])

# class student:
#     def display(self):
#         print("hello students")
#         print("welcome to python programing")

# s1=student()

# s1.display()

# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
    
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("marks:",self.marks)

# s1=student("syed",21,87)
# s2=student("abbas",22,97)
# s1.display()
# s2.display()

# class student:
#     def __init__(self):
#         self.__marks=0

#     def set_marks(self,marks):
#         self.__marks=marks

#     def show_marks(self):
#         print("student marks:",self.__marks)

#         s1=student()
#         s1.set_marks(85.5)
#         s1.show_marks()

# class grandfather:
#     def land(self):
#         print ("grandfather has a land")

# class father(grandfather):
#     def house(self):
#         print("father has a house")

# class son(father):
#     def car(self):
#         print("son has a car")

# s=son()
# s.land()
# s.house()
# s.car()

# class father:
#     def land(self):
#         print("father has a land")

# class son(father):
#     def house(self):
#         print("son has house")

# class daughter(father):
#     def car(self):
#         print("daughter has a car")

# s=son()
# d=daughter()
# s.land()
# s.house()
# d.land()
# d.car()

# class animal:
#     def sound(self):
#         print("animal makes a sound")

# class dog(animal):
#     def sound(self):
#         print("dog barks")

# class cat(animal):
#     def sound(self):
#         print("cat meows")

# animals=[dog(),cat(),animal()]
# for animal in animals:
#     animal.sound()


###########abstract class######
from abc import ABC,abstractmethod   

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class upi(payment):
    def pay(self,amount):
        print("paid {amount} using UPI")

class card(payment):
    def pay(self,amount):
        print("paid (amount) using card")

p1=upi()
p2=card()
p1.pay(1000)
p2.pay(2000)