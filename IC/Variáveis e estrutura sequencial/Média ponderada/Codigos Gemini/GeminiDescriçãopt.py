# filename: grades_calc.py
grades = []
for i in range(4):
    grade = float(input("Enter grade {}: ".format(i)))
    grades.append(grade)
avg = sum(grades) / len(grades)
print("Average: {}".format(avg))
