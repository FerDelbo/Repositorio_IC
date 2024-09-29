def speed_infractions(speeds):
    max_speed = speeds[0]
    infractions = []
    for i in range(1, len(speeds)):
        speed = speeds[i]
        if speed > max_speed * 1.2 and speed < max_speed * 1.5:
            infractions.append(i)
    return infractions, len(infractions)

from numpy import*#minha adição
speeds = array(eval(input()))#minha adição
#speeds = [60.0, 73.9, 22.9, 72.1, 72.0, 100.6]#codigo original
infractions, count = speed_infractions(speeds)
for i in infractions:
    print(i)
print(count)