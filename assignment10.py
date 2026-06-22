# =====================================
# Question 1: Create student.txt and write your name
# =====================================

file = open("student.txt", "w")
file.write("Rohit More")
file.close()

print("Name written successfully.")

# =====================================
# Question 2: Read data from student.txt
# =====================================

file = open("student.txt", "r")
data = file.read()
print("\nFile Content:")
print(data)
file.close()

# =====================================
# Question 3: Append your city name
# =====================================

file = open("student.txt", "a")
file.write("\nPune")
file.close()

print("\nCity name appended successfully.")

# =====================================
# Question 4: Read the file using readline()
# =====================================

file = open("student.txt", "r")
print("\nReading line by line:")
print(file.readline())
print(file.readline())
file.close()

# =====================================
# Question 5: Check whether a file exists or not
# =====================================

import os

if os.path.exists("student.txt"):
    print("\nFile exists.")
else:
    print("\nFile does not exist.")

# =====================================
# Question 6: Store 5 student names in a file and display them
# =====================================

names = ["Rohit", "Rahul", "Amit", "Priya", "Sneha"]

file = open("students.txt", "w")

for name in names:
    file.write(name + "\n")

file.close()

file = open("students.txt", "r")

print("\nStudent Names:")
print(file.read())

file.close()