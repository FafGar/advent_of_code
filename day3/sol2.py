fin = open('input.txt')
lines = fin.readlines()

part_nums = []
schematic = []
for line in lines:
    map_line = []
    cur_num = None
    for char in line:
        if char.isnumeric():
            if(cur_num is not None):
                cur_num += char
            else:
                cur_num = char
            
            map_line.append(len(part_nums))
        else:
            if char =='*':
                map_line.append(-2)
            elif char != '.':
                map_line.append(-1)
            else:
                map_line.append(None)
            if(cur_num is not None):
                part_nums.append(int(cur_num))
                cur_num = None

    schematic.append(map_line)


directions = [
    (-1,-1),(0,-1),(1,-1),
    (-1,0),       (1,0),
    (-1,1),(0,1),(1,1)
]

total = 0;
total_gear = 0;
for line in range(1,len(schematic)-1,1):
    for point in range(1,len(schematic[line])-1,1):
        if(schematic[line][point] in (-1,-2)):
            used = []
            for x,y in directions:
                if schematic[line+y][point+x] is not None and schematic[line+y][point+x] > -1 and schematic[line+y][point+x] not in used:
                    used.append(schematic[line+y][point+x])
                    total+=part_nums[schematic[line+y][point+x]]
            if(schematic[line][point] == -2 and len(used) == 2):
                total_gear += part_nums[used[0]] * part_nums[used[1]]


print(total)
print(total_gear)





