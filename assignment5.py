# =========================
# Challenge 1: Student Management System
# =========================

class Student:
    school_name = "ABC College"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_student(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}, School: {Student.school_name}")

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


s1 = Student("Rohit", 18, "AIML")
s2 = Student("Amit", 19, "Computer Science")

print("\n=== Student Details Before Change ===")
s1.display_student()
s2.display_student()

Student.change_school_name("XYZ College")

print("\n=== Student Details After Change ===")
s1.display_student()
s2.display_student()


# =========================
# Challenge 2: Employee Counter
# =========================

class Employee:
    employee_count = 0

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee(self):
        print(f"ID: {self.emp_id}, Name: {self.emp_name}, Salary: {self.salary}")

    @classmethod
    def show_total_employees(cls):
        print("Total Employees:", cls.employee_count)


e1 = Employee(101, "Rahul", 30000)
e2 = Employee(102, "Priya", 35000)
e3 = Employee(103, "Karan", 40000)

print("\n=== Employee Details ===")
e1.display_employee()
e2.display_employee()
e3.display_employee()

Employee.show_total_employees()


# =========================
# Challenge 3: Bank Account System
# =========================

class BankAccount:
    bank_name = "State Bank of India"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn.")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name


acc1 = BankAccount(12345, "Rohit", 5000)
acc2 = BankAccount(67890, "Raj", 8000)

print("\n=== Bank Account Operations ===")
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.check_balance()

BankAccount.change_bank_name("HDFC Bank")
print("New Bank Name:", BankAccount.bank_name)


# =========================
# Challenge 4: Mobile Store Inventory
# =========================

class Mobile:
    discount_percentage = 10

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_mobile(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

    def calculate_discount_price(self):
        discount = self.price * Mobile.discount_percentage / 100
        return self.price - discount

    @classmethod
    def change_discount(cls, new_discount):
        cls.discount_percentage = new_discount


m1 = Mobile("Samsung", "Galaxy S24", 80000)
m2 = Mobile("Apple", "iPhone 15", 90000)

print("\n=== Mobile Details ===")
m1.display_mobile()
print("Discount Price:", m1.calculate_discount_price())

Mobile.change_discount(20)

print("New Discount Price:", m1.calculate_discount_price())


# =========================
# Challenge 5: Library Book Management
# =========================

class Book:
    library_name = "City Library"

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book_info(self):
        print(
            f"Book ID: {self.book_id}, "
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Library: {Book.library_name}"
        )

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name


b1 = Book(1, "Python Basics", "John")
b2 = Book(2, "AI Fundamentals", "David")
b3 = Book(3, "Data Science", "Smith")

print("\n=== Books Before Change ===")
b1.display_book_info()
b2.display_book_info()
b3.display_book_info()

Book.change_library_name("Central Library")

print("\n=== Books After Change ===")
b1.display_book_info()
b2.display_book_info()
b3.display_book_info()