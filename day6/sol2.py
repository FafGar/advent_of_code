fin =  open('input.txt')
time_line, dist_line = fin.readlines()

times = time_line.split()[1:]
dists = dist_line.split()[1:]

time = ""
dist = ""
for i in range(len(times)):
    time+=times[i]
    dist+=dists[i]

time = int(time)
dist = int(dist)
counter = 0
for j in range(time):
    if (time-j) * j > dist: counter+=1

print(counter)