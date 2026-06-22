# ==============================
# Python Modules & OOP Challenges (1-30)
# ==============================

import math
import random

# ------------------------------
# Challenge 1
# ------------------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Challenge 1")
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

# ------------------------------
# Challenge 2
# ------------------------------
employee_name = "Rohit"
salary = 25000

def display_employee():
    print("Name:", employee_name)
    print("Salary:", salary)

print("\nChallenge 2")
display_employee()

# ------------------------------
# Challenge 3
# ------------------------------
print("\nChallenge 3")
print("Square Root of 144 =", math.sqrt(144))
print("Pi =", math.pi)
print("Factorial of 6 =", math.factorial(6))

# ------------------------------
# Challenge 4
# ------------------------------
print("\nChallenge 4")
print("Random Number:", random.randint(1, 100))
print("Random Choice:", random.choice(['Python', 'Java', 'React', 'Django']))

# ------------------------------
# Challenge 5
# ------------------------------
def area_circle(r):
    return math.pi * r * r

def area_rectangle(l, w):
    return l * w

print("\nChallenge 5")
print("Circle Area:", area_circle(5))
print("Rectangle Area:", area_rectangle(4, 6))

# ------------------------------
# Challenge 6
# ------------------------------
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Rohit", 18)
print("\nChallenge 6")
print(s.name, s.age)

# ------------------------------
# Challenge 7
# ------------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Fortuner")
car2 = Car("Hyundai", "Creta")

print("\nChallenge 7")
print(car1.brand, car1.model)
print(car2.brand, car2.model)

# ------------------------------
# Challenge 8
# ------------------------------
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

print("\nChallenge 8")
b1 = Book("Python", "ABC", 500)
b2 = Book("Java", "XYZ", 600)
b3 = Book("C++", "PQR", 700)

for b in [b1, b2, b3]:
    print(b.title, b.author, b.price)

# ------------------------------
# Challenge 9
# ------------------------------
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

l1 = Laptop("Dell", "8GB", 50000)
l2 = Laptop("HP", "16GB", 65000)

print("\nChallenge 9")
print(l1.brand, l1.ram, l1.price)
print(l2.brand, l2.ram, l2.price)

# ------------------------------
# Challenge 10
# ------------------------------
class Mobile:
    def __init__(self, company, model, storage):
        self.company = company
        self.model = model
        self.storage = storage

print("\nChallenge 10")
m1 = Mobile("Samsung", "A54", "128GB")
m2 = Mobile("Realme", "Narzo", "256GB")
print(m1.company, m1.model, m1.storage)
print(m2.company, m2.model, m2.storage)

# ------------------------------
# Challenge 11
# ------------------------------
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

print("\nChallenge 11")
e = Employee(101, "Rohit", 30000)
print(e.emp_id, e.emp_name, e.salary)

# ------------------------------
# Challenge 12
# ------------------------------
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

print("\nChallenge 12")
a1 = BankAccount(1111, "Rohit", 5000)
a2 = BankAccount(2222, "Ram", 8000)
print(a1.account_number, a1.holder_name, a1.balance)
print(a2.account_number, a2.holder_name, a2.balance)

# ------------------------------
# Challenge 13
# ------------------------------
class Movie:
    def __init__(self, movie_name, hero, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.rating = rating

print("\nChallenge 13")
m = Movie("Pushpa", "Allu Arjun", 5)
print(m.movie_name, m.hero, m.rating)

# ------------------------------
# Challenge 14
# ------------------------------
class Product:
    def __init__(self, pid, pname, price):
        self.pid = pid
        self.pname = pname
        self.price = price

print("\nChallenge 14")
p1 = Product(1, "Laptop", 50000)
p2 = Product(2, "Mouse", 500)
print(p1.pname, p1.price)
print(p2.pname, p2.price)

# ------------------------------
# Challenge 15
# ------------------------------
class College:
    def __init__(self, cname, city, count):
        self.cname = cname
        self.city = city
        self.count = count

print("\nChallenge 15")
c = College("ABC College", "Pune", 1000)
print(c.cname, c.city, c.count)

# ------------------------------
# Challenge 16-20
# ------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

print("\nChallenge 16")
Person("Rohit", 18).display()

class Animal:
    def __init__(self, animal_name, color):
        self.animal_name = animal_name
        self.color = color

    def show(self):
        print(self.animal_name, self.color)

print("\nChallenge 17")
Animal("Dog", "Black").show()

class Vehicle:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print(self.company, self.model)

print("\nChallenge 18")
Vehicle("Honda", "City").display()

class Teacher:
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject

    def display(self):
        print(self.teacher_name, self.subject)

print("\nChallenge 19")
Teacher("Patil", "Python").display()

class Player:
    def __init__(self, player_name, team):
        self.player_name = player_name
        self.team = team

    def display(self):
        print(self.player_name, self.team)

print("\nChallenge 20")
Player("Virat", "India").display()

# ------------------------------
# Challenge 21-25
# ------------------------------
print("\nChallenge 21-25")
s1 = {"name":"A","roll":1,"marks":80}
s2 = {"name":"B","roll":2,"marks":85}
s3 = {"name":"C","roll":3,"marks":90}
print(s1)
print(s2)
print(s3)

# ------------------------------
# Challenge 26
# ------------------------------
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

print("\nChallenge 26")
r = Rectangle(5, 4)
print(r.calculate_area())

# ------------------------------
# Challenge 27
# ------------------------------
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

print("\nChallenge 27")
c = Circle(5)
print(c.calculate_area())

# ------------------------------
# Challenge 28
# ------------------------------
class EmployeeSalary:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

print("\nChallenge 28")
emp = EmployeeSalary(30000)
print(emp.annual_salary())

# ------------------------------
# Challenge 29
# ------------------------------
class StudentPercentage:
    def __init__(self, marks, total):
        self.marks = marks
        self.total = total

    def calculate_percentage(self):
        return (self.marks / self.total) * 100

print("\nChallenge 29")
sp = StudentPercentage(450, 500)
print(sp.calculate_percentage())

# ------------------------------
# Challenge 30
# ------------------------------
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

print("\nChallenge 30")
b = Bank(1000)
b.deposit(500)
b.withdraw(200)
print("Balance =", b.balance)