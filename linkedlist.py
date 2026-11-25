class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)
five=Node(50)

# Connect nodes here
first.next=second
second.next=third
third.next=fourth
fourth.next=five


# Create head here
current=first
count=0

# Traverse and print here
while current :
    print(current.data,end="->")
    current=current.next
    count+=1

print(None)
print(count)

# Find middle
mid = count // 2

current =first

for i in range(mid):
    current = current.next

print(current.data)

# ----------------------------------------------------------------------------------------
# LeetCode #876 – Middle of the Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = [1, 2, 3, 4, 5]

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


