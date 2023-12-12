fin = open('input.txt')
lines = fin.readlines()


total = 0
for line in lines:
    segments = line.split(":")
    sets = segments[1].split(';')

    minimums = {'red':0,
            'green':0,
            'blue': 0}
    for set in sets:
        colors = set.split(',')
        for color in colors:
            pieces = color.strip().split(' ')
            if (int(pieces[0]) > minimums[pieces[1]]): minimums[pieces[1]]  = int(pieces[0]) 
        
    total += minimums['green'] * minimums['red'] * minimums['blue'] 

print(total)