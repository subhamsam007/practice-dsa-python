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


# 496. Next Greater Element I


nums1 = [4,1,2] 
nums2 = [1,3,4,2]

stk=[]
ans={}

for i in range(len(nums2)-1,-1,-1):
    while len(stk)>0 and stk[-1]<=nums2[i]:
        stk.pop()

    if not stk: # len(stack)==0
        ans[nums2[i]]=-1
    else:
        ans[nums2[i]]=stk[-1]
    stk.append(nums2[i])

seen=[]
for x in nums1:
    seen.append(ans[x])
print(seen)
print(ans)

print(stk)


# 739. Daily Temperatures
tem=[30,40,50,60]
res=[0]*len(tem)
s=[]
for i in range(len(tem)-1,-1,-1):
    while len(s)>0 and tem[s[-1]]<=tem[i]:
        s.pop()
    if len(s)==0:
        res[i]=0
    else:
        res[i]=s[-1]-i
    s.append(i)
print(res)

# -----------------------------------------------------------------------
# 1209. Remove All Adjacent Duplicates in String II

s = "deeed"
k = 3

st=[]

for i in s:
    if len(st)==0 or  st[-1][0] != i:
        st.append([i,1])
    else:
         st[-1][1] += 1

         if st[-1][1]==k:
             st.pop()
print(st)
anss=""
# for j in st:
#     anss+=j[0]*j[1]
# print(anss)

for char,j in st:
    anss+= char*j
print(anss)