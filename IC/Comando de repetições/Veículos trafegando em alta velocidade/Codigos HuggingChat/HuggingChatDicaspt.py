def speed_violations(speed_records):
    max_speed = speed_records[0]
    violations = []
    for i in range(1, len(speed_records)):
        current_speed = speed_records[i]
        if current_speed > max_speed * 1.2 and current_speed < max_speed * 1.5:
            violations.append(i)
    return violations, len(violations)

#speed_records = [100, 110, 125, 130, 140, 150, 160, 170, 180]
speed_records = input()
violations, count = speed_violations(speed_records)
for violation in violations:
    print(violation)
#print("Total violations:", count)
print(count)