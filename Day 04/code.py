#CLASS = blueprint of object, Object = instance of class

# class Student:
#     subject = "Python"
#     college = "MMMUT"
#     year = "3rd year"

# stu1 = Student()
# stu2 = Student()
# print(stu1.subject, stu1.college, stu1.year)
# print(stu2.subject, stu2.college, stu2.year)
# #type
# print(type(stu1))
# #list
# l = [1, 2]
# print(type(l))
# #set
# s = set()
# print(type(s))

#CONSTRUCTOR =  __init__()method
# ek constructor me ek init method run krta h 

# class Student:
#     def __init__(self): #default
#         print("obj is being constructed..")

#     def __init__(self, name,  cgpa): #parametrized
#         self.name = name
#         self.cgpa = cgpa
    
#     def get_cgpa(self):
#         return self.cgpa
    
# stu1 = Student("Satyam", 6.4)
# stu2 = Student("Urvashi", 8.4)
# stu3 = Student("Shradha", 9.2)

# print(stu1.name, stu1.cgpa)
# print(stu2.name, stu2.cgpa)
# print(stu3.name, stu3.cgpa)

# print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

#ATTRIBUTES

# class Student:
#     college_name = "MMMUT College" #class
#     PI = 3.1
#     def __init__(self, name, cgpa):
#         self.name = name #instance
#         self.cgpa = cgpa
#         self.PI = 3.14

# stu1 = Student("Satyam", 6.4)
# print(stu1.PI)
# print(Student.PI)

#METHODS (instance, class & static)
# instance

# class Laptop:
#     storage_type = "ssd"

#     def __init__(self, RAM, storage):
#         self.RAM = RAM
#         self.storage = storage

#     @classmethod
#     def get_storage_type(cls): #class method
#         print(f"storage type = {cls.storage_type}")

#     def  get_info(self): #instance method
#         print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

#     @staticmethod
#     def calc_discount(price, discount):
#         final_price = price - (discount * price / 100)
#         print(f"discounted price = {final_price}")

# l1 = Laptop("16gb", "512gb")
# # l2 = Laptop("8gb", "256gb")

# # l1.get_info()

# # Laptop.get_storage_type()

# l1.calc_discount(40_000, 10)

#Problem (Product Store)

#Q = Design & create an online store for product (name, price).
#Track total products being created.
#Create a static method to calculate discount on each product based on a % parameter

# class Product:
#     count = 0

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         Product.count += 1

#     def get_info(self): #instance method
#             print(f"price of {self.name} is Rs. {self.price}")

#     @classmethod
#     def get_count(cls):
#          print(f"total products in store = {cls.count}")

#     @staticmethod
#     def calc_discount(price, discount):
#          print(f"discounted price = {price - (price * discount / 100)}")

# p1 = Product("phone", 10_000)
# p2 = Product("laptop", 50_000)
# p3 = Product("pen", 10)

# p1.get_info()

# Product.get_count()

# p1.calc_discount(p1.price, 12)

#PILLER OF OOPs

#ENCAPSULATION => wrapping data & function into single unit

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name #public
#         self._balance = balance #protected but __use then private (data mangling)
    
#     def get_balance(self): #getter
#         return self.__balance
    
#     def set_balance(self, newBalnace): #setter
#         self.__balance = newBalnace

# acc1 = BankAccount("Satyam Chaudhary", 100_000)

# acc1.set_balance(200_000)

# print(acc1.name, acc1._balance)

# print(acc1.name, acc1._BankAccount__balance)

#INHERITENCE => reusing attribute & methods from a parent class

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

#     def change_time(self, new_end_time):
#         self.end_time = new_end_time

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role)
#         self.salary = salary

# # t1 = Teacher("Math")
# # t1.change_time("5pm")

# acc1 = Accountant(25_000, "CA")

# # staff1 = AdminStaff("manager")

# # print(t1.subject, t1.start_time, t1.end_time)
# # print(staff1.role, staff1.start_time, staff1.end_time)
# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)

#TYPES OF INHERITENCE
#Multiple Inheritence

# class Teacher:
#     def __init__(self, salary):
#         self.salary = salary

# class Students:
#     def __init__(self, cgpa):
#         self.cgpa = cgpa

# class TA(Teacher, Students):
#     def __init__(self, salary, cgpa, name):
#         super().__init__(salary)
#         Students.__init__(self, cgpa)
#         self.name = name
# ta1 = TA(15_000, 6.4, "Satyam")

# print(ta1.name, ta1.cgpa, ta1.salary)

#ABSTRACTION => hiding internal details & showing only essential features

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound():
#         pass

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")

# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")

# lion = Lion()
# lion.make_sound()

# cow = Cow()
# cow.make_sound()

#POLYMORPHISM => many forms

#01 Function Overriding

# class Employee:
#     def ge_designation(self):
#         print("designation = Employee")

# class Teacher(Employee):
#     def ge_designation(self):
#         print("designation = Teacher")

# t1 = Teacher()
# t1.ge_designation()

#02 Duck Typing

# class Teacher():
#     def get_designation(self):
#         print("designation = Teacher")

# class Accountant():
#     def get_designation(self):
#         print("designation = Accountant")

# t1 = Teacher()
# t1.get_designation()

# acc1 = Accountant()
# acc1.get_designation()