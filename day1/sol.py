import re

fin = open('input.txt')
lines = fin.readlines()

numMap = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0;
for line in lines:
    matches = []
    for i in range(len(line)):
        if line[i].isnumeric():
            matches.append(line[i])
        else:
           for add in [2,3,4]:
               temp = line[i:i+add+1]
               if temp in numMap:
                   matches.append(str(numMap.index(temp)+1))
            
    total += int(matches[0] + matches[-1])

print(total)