from abc import ABC, abstractmethod

# ==================================
# Question 1: Abstract Class & Abstract Method
# ==================================

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

c = Car()
c.start()

print()

# ==================================
# Question 2: Abstract Class with Multiple Child Classes
# ==================================

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()

print()

# ==================================
# Question 3: Polymorphism Using Method Overriding
# ==================================

class Shape:
    def draw(self):
        print("Drawing Shape")

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

c = Circle()
r = Rectangle()

c.draw()
r.draw()

print()

# ==================================
# Question 4: Polymorphism with Loop
# ==================================

class Bird:
    def fly(self):
        print("Bird flies")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies low")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies high")

birds = [Sparrow(), Eagle()]

for bird in birds:
    bird.fly()

print()

# ==================================
# Question 5: Abstract Class + Polymorphism
# ==================================

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Designer(Employee):
    def work(self):
        print("Designer creates UI designs")

employees = [Developer(), Designer()]

for emp in employees:
    emp.work()