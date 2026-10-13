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

# 3-3 sum closest to the target
# Triplets with Smaller Sum
#   print all triplets with sum smaller than the target sum
sum = 12
arrr = [5, 1, 3, 4, 7]
count = 0

arrr.sort()
nf =len(arrr)

for i in range(nf-2):
    l =i+1
    r=nf-1
    while l<r:
        total = arrr[i] + arrr[l] + arrr[r]
        if total < sum:
            count += (r-l)
            # for k in range(r,l,-1):
            #     print([arrr[i],arrr[l],arrr[k]])
            l+=1
        else:
            r-=1

print(count)


# 4-dutch national flag problem Sort Colors
colors = [2,0,2,1,1,0]
# brute force
zero =[]
one = []
two = []
for i in colors:
    if i == 0:
        zero.append(i)
    elif i == 1:
        one.append(i)
    else:
        two.append(i)
print(zero + one + two)
# optimized solution with out two pointer 
zero = 0
one = 0
two = 0
for i in colors:
    if i==0:
        zero+=1
    elif i==1:  
        one+=1
    else:
        two+=1
print([0]*zero + [1]*one + [2]*two)
# optimized solution with two pointer
start = 0
mid = 0
end = len(colors) - 1

while mid <= end:

    if colors[mid] == 0:
        colors[start], colors[mid] = colors[mid], colors[start]
        start += 1
        mid += 1

    elif colors[mid] == 1:
        mid += 1

    else:
        colors[mid], colors[end] = colors[end], colors[mid]
        end -= 1

print(colors)

# 5- Is Subsequence

s = "abs" 
t = "ahbdgdc"
i = 0
j =0
while i<len(s) and j<len(t):
    if s[i] == t[j]:
        i+=1
    else:
        j+=1
if i == len(s):
    print(True)
else:
    print(False)