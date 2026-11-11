
# Student Marks Calculator

print("===== STUDENT MARKS CALCULATOR =====")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

print("\n===== RESULT =====")
print("Student:", name)
print("Total Marks:", total, "/ 500")
print("Average:", average)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
print("Thank you for using the calculator!")
