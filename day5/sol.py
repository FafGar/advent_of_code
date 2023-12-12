fin = open('input.txt')
lines = fin.read()



spliter = '''

'''
sections = lines.split(spliter)
seeds = [int(x) for x in sections[0].split()[1:]]

maps = sections[1:]

for section in maps:
    new_seeds = list(seeds)
    lines = section.split('\n')
    for j in range(1,len(lines),1):
        dest,source,step = lines[j].split()
        dest = int(dest)
        source = int(source)
        step = int(step)
        for i in range(len(seeds)):
            if seeds[i] in range(source,source+step,1):
                new_seeds[i] += dest-source
    seeds = list(new_seeds)

print(min(seeds))
