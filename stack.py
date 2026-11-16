# Reverse a String
str= "madam"
stack=[]

for i in str:
    stack.append(i)
print(stack)

rev= ""

while(len(stack)>0):
    rev+=stack.pop()
print(rev)
# palindrome
if str == rev:
    print("pallendrom")
else:
    print("No")

# next greater elemnt 

nums = [4, 7, 2, 9, 3]

st=[-1]*len(nums)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] > nums[i]:
            st[i]=nums[j]
            break
print(st)

#  optimize way 

ans=[0]*len(nums)
stackk=[]

for i in range(len(nums)-1,-1,-1):
    while stackk and  stackk[-1]<= nums[i]:
        stackk.pop()
    if len(stackk)==0:
        ans[i]=-1
    else:
        ans[i]=stackk[-1]

    stackk.append(nums[i])

print(ans)
