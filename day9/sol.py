def evaluate(nums:list) -> int:
    new_nums = []
    zero_only = True
    for i in range(1,len(nums),1):
        num = nums[i] - nums[i-1]
        new_nums.append(num)
        if(num != 0):zero_only = False

    if(zero_only):
        return nums[-1]
    else:
        return nums[-1] + evaluate(new_nums)



fin = open('input.txt')
lines = fin.readlines()


total = 0
for line in lines:
    total+=evaluate([int(val) for val in line.split()])

print(total)