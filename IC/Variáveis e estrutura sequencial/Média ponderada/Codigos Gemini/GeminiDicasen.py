# filename: weighted_average.py
#print("Enter the first note:")
note1 = float(input())
#print("Enter the second note:")
note2 = float(input())
#print("Enter the third note:")
note3 = float(input())
#print("Enter the fourth note:")
note4 = float(input())

weighted_average = (note1 * 1 + note2 * 2 + note3 * 3 + note4 * 4) / (1 + 2 + 3 + 4)
#print(f"The weighted average is: {round(weighted_average, 1)}")
print(round(weighted_average, 1))
