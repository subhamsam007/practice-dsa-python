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
# Maximum Product Subarray of the 
n = [-2,3,4]
max_best=n[0]
min_best=n[0]
res=n[0]
for i in range(1,len(n)):
    f1=n[i]
    f2=max_best*n[i]
    f3=min_best*n[i]
    max_best=max
    max_end=max(f1,max(f2,f3))
    min_end=min(f1,min(f2,f3))
    max_best = max_end
    min_best = min_end
    res=max(res,max_best)
print(res)