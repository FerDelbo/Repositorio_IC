# filename: speed_violations.py
import csv

with open('speed_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    violations = []
    for row in reader:
        speed_limit = int(row[1])
        speed = int(row[2])
        if speed > speed_limit * 1.2 and speed < speed_limit * 1.5:
            violations.append(row)

print(f'Motoristas que infringiram o limite de velocidade em mais de 20% e menos que 50% acima da velocidade máxima permitida:')
for violation in violations:
    print(violation[0])
print(f'Total de motoristas que infringiram: {len(violations)}')
