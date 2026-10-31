nums = [-2,1,-3,4,-1,2,1,-5,4]
max_sum =nums[0]
for i in range(len(nums)):
    c_sum=0
    for j in range(i,len(nums)):
        c_sum+=nums[j]
        if c_sum>max_sum:
            max_sum=c_sum
print(max_sum)

# kadanes algorithm

best=nums[0]
ans=nums[0]
for i in range(len(nums)):
    v1=best+nums[i]
    v2=nums[i]
    best=max(v1,v2)
    ans=max(ans,best)
print(ans)