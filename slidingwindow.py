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