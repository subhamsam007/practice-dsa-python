# 1. Two Sum
nums = [2,7,11,15]
target = 9



# brute force 
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])

# optimized solution
result = {}
for i in range(len(nums)):
    need = target - nums[i]
    if need in result:
        print([result[need], i])

    result[nums[i]] = i
