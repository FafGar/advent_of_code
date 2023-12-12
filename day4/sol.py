fin = open('input.txt')
lines = fin.readlines()

total = 0;
for line in lines:
    numbers = line.split(':')[1]
    winners,yours  = numbers.split('|')

    
    power = -1
    nums = winners.split()
    your_nums = yours.split()
    for number in nums:
        if number in your_nums:
            power +=1
    if power >= 0:
        total += pow(2,power)
    
print(total)