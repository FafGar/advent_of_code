fin = open('input.txt')
lines = fin.readlines()

maximums = {'red':12,
            'green':13,
            'blue': 14}
total = 0
for line in lines:
    segments = line.split(":")
    sets = segments[1].split(';')
    id_num = int(segments[0].split(' ')[1])
    good = True;
    for set in sets:
        colors = set.split(',')
        for color in colors:
            pieces = color.strip().split(' ')
            # print(pieces)
            if (int(pieces[0]) > maximums[pieces[1]]): good = False
        
    if(good): total += id_num

print(total)