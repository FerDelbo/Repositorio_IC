# filename: average.py
grades = []
for i in range(4):
    grades.append(float(input(f"Digite a {i+1}ª nota: ")))
average = (grades[0] * 1 + grades[1] * 2 + grades[2] * 3 + grades[3] * 4) / 10
print(round(average, 1))
