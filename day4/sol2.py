fin = open('input.txt')
lines = fin.readlines()

card_counts = [1 for line in lines]
for line_num in range(len(lines)):
    numbers = lines[line_num].split(':')[1]
    winners,yours  = numbers.split('|')

    nums = winners.split()
    your_nums = yours.split()
    for iter in range(card_counts[line_num]):
        count = 0
        for number in nums:
            if number in your_nums:
                count +=1
                card_counts[line_num+count] += 1


    
print(sum(card_counts))