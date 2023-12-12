import math

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

curr_locations  = []
for key in locations.keys():
    if key[-1] =="A": curr_locations.append(key)


counts = []
for loc  in curr_locations:
    curr_location = loc
    count = 0
    index = 0
    noZ = True
    while noZ:
        count+=1
        if(instructions[index] == 'R'):
            curr_location = locations[curr_location][1]
        else:
            curr_location = locations[curr_location][0]
        index+=1
        if index >= len(instructions): index = 0

        noZ = False
        if curr_location[-1] != 'Z': noZ = True
    counts.append(count)

print(counts)

curr_total = counts[0]
for i in range(1,len(counts),1):
    curr_total = abs(curr_total*counts[i]) // math.gcd(curr_total,counts[i])
print(curr_total)
#There's defo a smarter way to do this but I don't feel like it
# Probably like find the length of all of them individually and find the smallest common multiple or something