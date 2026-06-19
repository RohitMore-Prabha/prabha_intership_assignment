# ==========================================
# PYTHON OOP PRACTICAL ASSIGNMENT (Q1-Q25)
# ==========================================

# Q1
print("\n===== Q1 Student Class =====")
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Rohit", 18)
s2 = Student("Amit", 19)
s3 = Student("Neha", 20)
s1.display()
s2.display()
s3.display()


# Q2
print("\n===== Q2 Employee Class =====")
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.emp_id, self.name, self.salary)

e = Employee(101, "Rohit", 25000)
e.display()


# Q3
print("\n===== Q3 Car Class =====")
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand, self.model)

c = Car("Toyota", "Fortuner")
c.display()


# Q4
print("\n===== Q4 BankAccount =====")
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

acc = BankAccount()
acc.deposit(5000)
acc.withdraw(1000)
print("Balance:", acc.balance)


# Q5
print("\n===== Q5 Book Class =====")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b1 = Book("Python", "Guido")
b2 = Book("AI", "John")
print(b1.title, b1.author)
print(b2.title, b2.author)


# Q6
print("\n===== Q6 Mobile Class =====")
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print(self.brand, self.price)

m = Mobile("Samsung", 20000)
m.display()


# Q7
print("\n===== Q7 Company Class =====")
class Company:
    company_name = "Prabha Technology"

c1 = Company()
c2 = Company()

print(c1.company_name)
print(c2.company_name)


# Q8
print("\n===== Q8 Product Class =====")
class Product:
    tax_rate = 0.18

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price + self.price * Product.tax_rate

p = Product(1000)
print("Final Price:", p.final_price())


# Q9
print("\n===== Q9 Student Class Method =====")
class StudentClass:
    school = "ABC School"

    @classmethod
    def update_school(cls, name):
        cls.school = name

StudentClass.update_school("XYZ School")
print(StudentClass.school)


# Q10
print("\n===== Q10 Vehicle Count =====")
class Vehicle:
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

v1 = Vehicle()
v2 = Vehicle()
v3 = Vehicle()

print("Total Vehicles:", Vehicle.vehicle_count)


# Q11
print("\n===== Q11 Calculator =====")
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

print(Calculator.add(10, 5))
print(Calculator.subtract(10, 5))
print(Calculator.multiply(10, 5))
print(Calculator.divide(10, 5))


# Q12
print("\n===== Q12 Temperature Converter =====")
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))


# Q13
print("\n===== Q13 Even/Odd =====")
class Utility:
    @staticmethod
    def check(num):
        return "Even" if num % 2 == 0 else "Odd"

print(Utility.check(7))


# Q14
print("\n===== Q14 Person & Student =====")
class Person:
    def __init__(self, name):
        self.name = name

class StudentInherit(Person):
    pass

s = StudentInherit("Rohit")
print(s.name)


# Q15
print("\n===== Q15 Vehicle & Bike =====")
class VehicleBase:
    def __init__(self, brand):
        self.brand = brand

class Bike(VehicleBase):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

b = Bike("Honda", "Shine")
print(b.brand, b.model)


# Q16
print("\n===== Q16 Shape =====")
class Shape:
    pass

class Circle(Shape):
    def area(self, r):
        return 3.14 * r * r

class Rectangle(Shape):
    def area(self, l, w):
        return l * w

print("Circle Area:", Circle().area(5))
print("Rectangle Area:", Rectangle().area(4, 6))


# Q17
print("\n===== Q17 Animal =====")
class Animal:
    pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

Dog().sound()
Cat().sound()


# Q18
print("\n===== Q18 Private Salary =====")
class PersonSalary:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

p = PersonSalary()
p.set_salary(50000)
print(p.get_salary())


# Q19
print("\n===== Q19 Encapsulation BankAccount =====")
class BankAccountPrivate:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

a = BankAccountPrivate()
a.deposit(3000)
print(a.get_balance())


# Q20
print("\n===== Q20 Employee Setter =====")
class EmployeePrivate:
    def __init__(self):
        self.__salary = 0

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e = EmployeePrivate()
e.set_salary(35000)
print(e.get_salary())


# Q21
print("\n===== Q21 Library Management =====")
class Library:
    def __init__(self, book):
        self.book = book

    def display(self):
        print("Book:", self.book)

l = Library("Python Programming")
l.display()


# Q22
print("\n===== Q22 Hospital Management =====")
class PersonHospital:
    def __init__(self, name):
        self.name = name

class Patient(PersonHospital):
    def display(self):
        print("Patient:", self.name)

p = Patient("Rohit")
p.display()


# Q23
print("\n===== Q23 School Management =====")
class School:
    school_name = "ABC School"

    @classmethod
    def change_name(cls, name):
        cls.school_name = name

    def display(self):
        print(self.school_name)

School.change_name("XYZ School")
School().display()


# Q24
print("\n===== Q24 Online Shopping System =====")
class ProductBase:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class MobileProduct(ProductBase):
    pass

m = MobileProduct("Samsung", 20000)
print(m.name, m.price)


# Q25
print("\n===== Q25 Mini ATM =====")
class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)

atm = ATM(5000)
atm.deposit(1000)
atm.withdraw(2000)
atm.show_balance()


print("\n_______________________________________________________________________________________________")