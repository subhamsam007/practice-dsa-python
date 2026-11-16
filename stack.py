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


nums = [4, 7, 2, 9, 3]

st=[-1]*len(nums)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] > nums[i]:
            st[i]=nums[j]
            break

    
print(st)