# filename: average.py
notes = []
for i in range(4):
    note = float(input("Enter note {0}: ".format(i+1)))
    notes.append(note)
average = (notes[0] + 2*notes[1] + 3*notes[2] + 4*notes[3]) / 10
print("The weighted average is {0:.2f}".format(average))
