fin = open('input.txt')
stuff  = fin.readlines()

instructions = stuff[0].strip()
stages = stuff[2:]
locations = {}

for stage in stages:
    pieces = stage.split('=')
    location = pieces[0].strip()
    directions = pieces[1].split(',')
    left = directions[0][2:]
    right = directions[1].strip('\n')[1:-1]

    locations[location] = (left,right)

curr_location = 'AAA'
count = 0
index = 0
while curr_location != "ZZZ":
    count+=1
    if(instructions[index] == 'R'):
        curr_location = locations[curr_location][1]
    else:
        curr_location = locations[curr_location][0]
    index+=1
    if index >= len(instructions): index = 0

print(count)