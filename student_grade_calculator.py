print("Student Grade Calculator")

name = input("Enter student name: ")

english = int(input("Enter marks in English: "))
maths = int(input("Enter marks in Maths: "))
physics = int(input("Enter marks in Physics: "))
computer = int(input("Enter marks in Computer: "))
chemistry = int(input("Enter marks in Chemistry: "))

total = english + maths + physics + computer + chemistry
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
