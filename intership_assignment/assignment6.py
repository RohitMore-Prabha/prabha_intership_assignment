# =====================================================
# Python OOP Assignment Solutions (Q1 - Q15)
# =====================================================

# =========================
# Question 1 (Hybrid Inheritance)
# =========================
print("\n===== Question 1 =====")

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def study(self):
        print(f"{self.name} is studying")

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")

class TeachingAssistant(Student, Teacher):
    def display(self):
        print("Name:", self.name)

ta = TeachingAssistant("Rohit")
ta.display()
ta.study()
ta.teach()

# =========================
# Question 2 (Hybrid Inheritance)
# =========================
print("\n===== Question 2 =====")

class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class ElectricCar(Car):
    def charge(self):
        print("Electric Car Charging")

class SportsElectricCar(ElectricCar):
    def speed(self):
        print("Sports Electric Car Running Fast")

sec = SportsElectricCar()
sec.start()
sec.charge()
sec.speed()

# =========================
# Question 3 (Hybrid Inheritance)
# =========================
print("\n===== Question 3 =====")

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def coding(self):
        print(f"{self.name} is coding")

class Manager(Employee):
    def manage(self):
        print(f"{self.name} is managing team")

class TechLead(Developer, Manager):
    pass

tl = TechLead("Amit")
tl.coding()
tl.manage()

# =========================
# Question 4 (Hybrid Inheritance)
# =========================
print("\n===== Question 4 =====")

class Person:
    def __init__(self, name):
        self.name = name

class Doctor(Person):
    def treat(self):
        print(f"Dr. {self.name} is treating patients")

class Nurse(Person):
    def assist(self):
        print(f"{self.name} is assisting doctor")

class HeadNurse(Nurse):
    def supervise(self):
        print(f"{self.name} supervises nurses")

hn = HeadNurse("Priya")
hn.assist()
hn.supervise()

# =========================
# Question 5 (Hierarchical Inheritance)
# =========================
print("\n===== Question 5 =====")

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow")

class Cow(Animal):
    def sound(self):
        print("Cow: Moo")

Dog().sound()
Cat().sound()
Cow().sound()

# =========================
# Question 6 (Hierarchical Inheritance)
# =========================
print("\n===== Question 6 =====")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    pass

class CurrentAccount(BankAccount):
    pass

class FixedDepositAccount(BankAccount):
    pass

s = SavingsAccount(10000)
c = CurrentAccount(20000)
f = FixedDepositAccount(50000)

print("Savings Balance:", s.balance)
print("Current Balance:", c.balance)
print("FD Balance:", f.balance)

# =========================
# Question 7 (Hierarchical Inheritance)
# =========================
print("\n===== Question 7 =====")

class Employee:
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Tester(Employee):
    def work(self):
        print("Tester tests software")

class Designer(Employee):
    def work(self):
        print("Designer creates UI")

Developer().work()
Tester().work()
Designer().work()

# =========================
# Question 8 (Hierarchical Inheritance)
# =========================
print("\n===== Question 8 =====")

class Shape:
    pass

class Circle(Shape):
    def area(self, r):
        return 3.14 * r * r

class Rectangle(Shape):
    def area(self, l, b):
        return l * b

class Square(Shape):
    def area(self, s):
        return s * s

print("Circle Area:", Circle().area(5))
print("Rectangle Area:", Rectangle().area(4, 6))
print("Square Area:", Square().area(4))

# =========================
# Question 9 (Polymorphism)
# =========================
print("\n===== Question 9 =====")

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Rectangle(Shape):
    def area(self):
        return 4 * 6

class Triangle(Shape):
    def area(self):
        return 0.5 * 4 * 8

shapes = [Circle(), Rectangle(), Triangle()]

for s in shapes:
    print("Area:", s.area())

# =========================
# Question 10 (Polymorphism)
# =========================
print("\n===== Question 10 =====")

class Payment:
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPIPayment(Payment):
    def pay(self):
        print("Paid using UPI")

class NetBankingPayment(Payment):
    def pay(self):
        print("Paid using Net Banking")

payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

for p in payments:
    p.pay()

# =========================
# Question 11 (Polymorphism)
# =========================
print("\n===== Question 11 =====")

class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Email Sent")

class SMSNotification(Notification):
    def send(self):
        print("SMS Sent")

class PushNotification(Notification):
    def send(self):
        print("Push Notification Sent")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for n in notifications:
    n.send()

# =========================
# Question 12 (Polymorphism)
# =========================
print("\n===== Question 12 =====")

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Lion(Animal):
    def make_sound(self):
        print("Roar")

animals = [Dog(), Cat(), Lion()]

for a in animals:
    a.make_sound()

# =========================
# Question 13 (Polymorphism)
# =========================
print("\n===== Question 13 =====")

class Employee:
    def role(self):
        pass

class Developer(Employee):
    def role(self):
        print("I am a Developer")

class Tester(Employee):
    def role(self):
        print("I am a Tester")

class Manager(Employee):
    def role(self):
        print("I am a Manager")

employees = [Developer(), Tester(), Manager()]

for e in employees:
    e.role()

# =========================
# Question 14 (Polymorphism)
# =========================
print("\n===== Question 14 =====")

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

class Bus(Vehicle):
    def start(self):
        print("Bus Started")

vehicles = [Car(), Bike(), Bus()]

for v in vehicles:
    v.start()

# =========================
# Question 15 (Polymorphism + Inheritance)
# =========================
print("\n===== Question 15 =====")

class Device:
    def operate(self):
        print("Device Operating")

class Camera(Device):
    def operate(self):
        print("Taking Photo")

class Phone(Device):
    def operate(self):
        print("Making Call")

class SmartPhone(Camera, Phone):
    def operate(self):
        print("SmartPhone: Calling and Taking Photos")

devices = [
    Camera(),
    Phone(),
    SmartPhone()
]

for d in devices:
    d.operate()

