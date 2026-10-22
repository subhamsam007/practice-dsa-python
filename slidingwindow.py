#  1-Max Sum Subarray of Size K
# brute force  with built-in function sum() with time complexity of O(n*k)
arr = [100, 200, 300, 400]
k = 2
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(len(arr) - k):
    window_sum = window_sum - arr[i] + arr[i + k] # arr[i+k] is the index of the new element that is added to the window
    max_sum = max(max_sum, window_sum)
print(max_sum)

# without built in function sum()

win_sum = 0
for i in range (k):
    win_sum  = win_sum + arr[i]
max_sum = win_sum
for i in range(len(arr) - k):
    win_sum = win_sum - arr[i] + arr[i + k]
    if win_sum > max_sum:
        max_sum = win_sum
print(max_sum)
# with while loop
window_sum = 0
high = k-1
low = 0
for i in range(low,high+1):
    window_sum += arr[i]
max_sum = window_sum
while high < len(arr)-1:
    window_sum = window_sum - arr[low] + arr[high+1]
    low += 1
    high += 1
    max_sum = max(max_sum, window_sum)
print(max_sum)

#  3 -209. Minimum Size Subarray Sum
#  brute force 
target = 4
csum = 0
numss = [1,4,4]
res=float('inf')
h=0
l=0
# while h < len(numss):
#     csum+= numss[h]
#     # print(csum)
#     while csum >= target:
#         print(f"sum: {csum}, h: {h}, l: {l}")
#         lens=h-l+1
#         res = min(res, lens)
#         csum -= numss[l]
#         l+=1
#     h+=1
# print(res)

while h < len(numss):
    csum+= numss[h]
    while csum >= target:
        length = h-l+1
        res = min(res, length)
        csum -= numss[l]
        l+=1  
    h+=1
print(res if res != float('inf') else 0)

#  Longest Substring with K Uniques
print("Longest Substring with K Uniques")
s = "aabacbebebe"
k = 3


low = 0
frequency = {}
res = -1
for i in range(len(s)):
    frequency[s[i]] = frequency.get(s[i], 0) + 1
    while len(frequency) > k:
        frequency[s[low]] -= 1
        if frequency[s[low]] == 0:
            del frequency[s[low]]
        low += 1

    if len(frequency) == k:
        res = max(res, i - low + 1)
print(frequency)
print(res)

# Fruit Into Baskets


fruits = [1,2,3,2,2]
f=fruits    
basket = {}
res=0
low = 0
for i in range(len(fruits)):
    basket[fruits[i]] = basket.get(fruits[i], 0) + 1
    while len(basket) > 2:
        basket[fruits[low]] -= 1
        if basket[fruits[low]] == 0:
            del basket[fruits[low]]
        low += 1
    
    res = max(res,i-low+1)
print(res)
# 3. Longest Substring Without Repeating Characters find the length of the longest substring without duplicate characters.
s = "pwwkew"
low=0
char=set()
res=0

for i in range(len(s)):
    while s[i] in char:
        char.remove(s[low])
        low+=1
    res = max(res, i-low+1)
    char.add(s[i])
print(res)
print(char)
