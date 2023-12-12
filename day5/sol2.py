fin = open('input.txt')
lines = fin.read()



spliter = '''

'''
sections = lines.split(spliter)
seeds = [int(x) for x in sections[0].split()[1:]]

proper_seeds= []
for seed_range in range(0,len(seeds),2):
    proper_seeds.append((seeds[seed_range],seeds[seed_range]+seeds[seed_range+1]-1))

maps = sections[1:]

for section in maps:
    new_seeds = list(proper_seeds)
    lines = section.split('\n')
    for j in range(1,len(lines),1):
        dest,source,step = lines[j].split()
        dest = int(dest)
        source = int(source)
        step = int(step)
        for i in range(len(proper_seeds)):
            if proper_seeds[i][0] >= source or proper_seeds[i][1] < source+step:
                new_seeds[i] += dest-source
    proper_seeds = list(new_seeds)

print(min(proper_seeds))
