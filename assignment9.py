# ====================================
# Question 1: Handle Division by Zero
# ====================================

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# ====================================
# Question 2: Handle Invalid Number Input
# ====================================

try:
    num = int(input("\nEnter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input. Please enter a number.")


# ====================================
# Question 3: Using try and except
# ====================================

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("\nEnter index: "))
    print("Element =", numbers[index])
except IndexError:
    print("Index out of range.")


# ====================================
# Question 4: Using else Block
# ====================================

try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)


# ====================================
# Question 5: Using finally Block
# ====================================

try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("File operation completed.")


# ====================================
# Question 6: Multiple Exceptions
# ====================================

numbers = [1, 2, 3, 4, 5]

try:
    num = int(input("\nEnter a number: "))
    index = int(input("Enter index: "))
    print("Element =", numbers[index])

except ValueError:
    print("Invalid input.")

except IndexError:
    print("Index out of range.")


# ====================================
# Question 7: Custom Exception
# ====================================

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("\nEnter a number: "))

    if num < 0:
        raise NegativeNumberError

    print("Entered number =", num)

except NegativeNumberError:
    print("Negative numbers are not allowed.")