# filename: weighted_average.py
notes = [float(x) for x in input().split()]
average = (notes[0] + 2 * notes[1] + 3 * notes[2] + 4 * notes[3]) / 10
print(round(average, 1))
