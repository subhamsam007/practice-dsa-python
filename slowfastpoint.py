# 1. Define the Node class (this is what LeetCode uses behind the scenes)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 2. Create the nodes using the class
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# 3. Link them together (and create a cycle pointing node4 back to node2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # <-- This creates the cycle!

head = node1

# 4. Your cycle-detection code
slow = head
fast = head
has_cycle = False

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        has_cycle = True
        break

print(has_cycle)  # This will now successfully print: True

# 287. Find the Duplicate Number leetcode  o(n2) and 0(1)
nums = [1,3,4,2,2]
n=len(nums)
# brute force 
for i in range (n):
    for j in range(i+1,n):
        if nums[i]==nums[j]:
            print(nums[i])
            break

# sorting by o(nlogn)and o(1)

nums.sort()
print(nums)
for i in range(n):
    if nums[i]==nums[i-1]:
        print(nums[i])
        break
# Floyd's Cycle-Finding Algorithm o(n) and 0(1)

slow =0
fast=0
while True:
    slow = nums[slow]
    fast= nums[nums[fast]]
    if slow==fast:
        break
slow =0
while slow!=fast:
    slow =nums[slow]
    fast= nums[fast]
print(slow,fast)
print("new ")
# 202. Happy Number
n=4
#  using hash map o(log n)and o(logn)
def get_next(x):
    total = 0

    while x > 0:
        x, digit = divmod(x, 10)
        total += digit **2

    return total


s=set()
while n!=1:
    if n in s:
        happy=False
        break
    s.add(n)
    n=get_next(n)
print(happy)