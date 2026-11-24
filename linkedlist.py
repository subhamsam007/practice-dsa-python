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