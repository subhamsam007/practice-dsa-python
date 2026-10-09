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
# -------------------------------------------------------------------------------------------------------------------------
# 2. 3 Sum or triplet sum

numss = [-1,0,1,2,-1,-4]
n=len(numss)
numss.sort()
# t=set()
# Brute force
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if numss[i] + numss[j] + numss[k] == 0:
#                 ti=[numss[i],numss[j],numss[k]]
#                 t.add(tuple(sorted(ti)))
# print(t)
# Optimized solution

result = []

for i in range(n-2):
    if i > 0 and numss[i] == numss[i-1]:
        continue
    left = i + 1
    right = n - 1

    while left < right:
        total = numss[i] + numss[left] + numss[right]
        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            result.append([numss[i], numss[left], numss[right]])
            while left < right and numss[left] == numss[left + 1]:
                left += 1
            while left < right and numss[right] == numss[right - 1]:
                right -= 1
            left += 1
            right -= 1
print(result)