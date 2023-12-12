fin =  open('input.txt')
time_line, dist_line = fin.readlines()

times = time_line.split()[1:]
dists = dist_line.split()[1:]

total = 1
for i in range(len(times)):
    dist = int(dists[i])
    time = int(times[i])

    counter = 0
    for j in range(time):
        if (time-j) * j > dist: counter+=1
    if counter>0: total*=counter

print(total)