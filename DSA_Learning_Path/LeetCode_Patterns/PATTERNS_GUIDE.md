# 🎯 LeetCode Patterns Mastery Guide

## Why Patterns Matter

Instead of solving 1000 random problems, master 14 patterns to solve 95% of LeetCode problems!

## 🔥 The 14 Essential Patterns

### 1️⃣ Sliding Window
**When to use:** Contiguous subarray/substring problems

**Problems:**
- Maximum sum subarray of size K
- Longest substring without repeating characters
- Minimum window substring
- Fruit into baskets

**Template:**
```python
def sliding_window(arr, k):
    window_start = 0
    max_sum = 0
    window_sum = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    return max_sum
```

**LeetCode Problems:**
- LC 3: Longest Substring Without Repeating Characters
- LC 76: Minimum Window Substring
- LC 209: Minimum Size Subarray Sum
- LC 424: Longest Repeating Character Replacement
- LC 567: Permutation in String

---

### 2️⃣ Two Pointers
**When to use:** Sorted arrays, palindromes, pair finding

**Problems:**
- Two sum (sorted array)
- Remove duplicates
- Container with most water
- 3Sum, 4Sum

**Template:**
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        if condition:
            # Process
            left += 1
        else:
            right -= 1
    
    return result
```

**LeetCode Problems:**
- LC 15: 3Sum
- LC 16: 3Sum Closest
- LC 11: Container With Most Water
- LC 42: Trapping Rain Water
- LC 75: Sort Colors

---

### 3️⃣ Fast & Slow Pointers (Floyd's Cycle Detection)
**When to use:** Linked list cycles, finding middle

**Problems:**
- Detect cycle in linked list
- Find cycle start
- Happy number
- Middle of linked list

**Template:**
```python
def has_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

**LeetCode Problems:**
- LC 141: Linked List Cycle
- LC 142: Linked List Cycle II
- LC 876: Middle of the Linked List
- LC 202: Happy Number
- LC 287: Find Duplicate Number

---

### 4️⃣ Merge Intervals
**When to use:** Overlapping intervals

**Problems:**
- Merge intervals
- Insert interval
- Meeting rooms
- Minimum meeting rooms

**Template:**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        if current[0] <= last[1]:
            # Overlapping - merge
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)
    
    return merged
```

**LeetCode Problems:**
- LC 56: Merge Intervals
- LC 57: Insert Interval
- LC 252: Meeting Rooms
- LC 253: Meeting Rooms II
- LC 435: Non-overlapping Intervals

---

### 5️⃣ Cyclic Sort
**When to use:** Arrays with numbers in range [1, n]

**Problems:**
- Find missing number
- Find duplicate
- Find all duplicates

**Template:**
```python
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1
    return nums
```

**LeetCode Problems:**
- LC 268: Missing Number
- LC 448: Find All Numbers Disappeared
- LC 442: Find All Duplicates
- LC 287: Find Duplicate Number
- LC 41: First Missing Positive

---

### 6️⃣ In-place Reversal of Linked List
**When to use:** Reverse linked list problems

**Template:**
```python
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev
```

**LeetCode Problems:**
- LC 206: Reverse Linked List
- LC 92: Reverse Linked List II
- LC 25: Reverse Nodes in k-Group
- LC 24: Swap Nodes in Pairs

---

### 7️⃣ Tree BFS (Level Order Traversal)
**When to use:** Level-by-level tree traversal

**Template:**
```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

**LeetCode Problems:**
- LC 102: Binary Tree Level Order Traversal
- LC 107: Binary Tree Level Order Traversal II
- LC 103: Binary Tree Zigzag Level Order
- LC 199: Binary Tree Right Side View
- LC 637: Average of Levels

---

### 8️⃣ Tree DFS (Depth First Search)
**When to use:** Path finding, tree recursion

**Template:**
```python
def dfs(root):
    if not root:
        return
    
    # Pre-order: Process root first
    process(root)
    dfs(root.left)
    dfs(root.right)
    
    # In-order: Process root between children
    # dfs(root.left)
    # process(root)
    # dfs(root.right)
    
    # Post-order: Process root last
    # dfs(root.left)
    # dfs(root.right)
    # process(root)
```

**LeetCode Problems:**
- LC 112: Path Sum
- LC 113: Path Sum II
- LC 257: Binary Tree Paths
- LC 129: Sum Root to Leaf Numbers
- LC 543: Diameter of Binary Tree

---

### 9️⃣ Two Heaps
**When to use:** Finding median, scheduling

**Template:**
```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (negative values)
        self.large = []  # min heap
    
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        
        # Balance
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

**LeetCode Problems:**
- LC 295: Find Median from Data Stream
- LC 480: Sliding Window Median
- LC 502: IPO

---

### 🔟 Subsets (Backtracking)
**When to use:** Generating combinations, permutations

**Template:**
```python
def subsets(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result
```

**LeetCode Problems:**
- LC 78: Subsets
- LC 90: Subsets II
- LC 46: Permutations
- LC 47: Permutations II
- LC 39: Combination Sum

---

### 1️⃣1️⃣ Modified Binary Search
**When to use:** Sorted or rotated arrays

**Template:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

**LeetCode Problems:**
- LC 33: Search in Rotated Sorted Array
- LC 81: Search in Rotated Sorted Array II
- LC 153: Find Minimum in Rotated Sorted Array
- LC 162: Find Peak Element
- LC 34: Find First and Last Position

---

### 1️⃣2️⃣ Top K Elements
**When to use:** Finding K largest/smallest elements

**Template:**
```python
import heapq

def top_k_frequent(nums, k):
    # Count frequency
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Use heap to find top k
    return heapq.nlargest(k, freq.keys(), key=freq.get)
```

**LeetCode Problems:**
- LC 215: Kth Largest Element
- LC 347: Top K Frequent Elements
- LC 373: Find K Pairs with Smallest Sums
- LC 378: Kth Smallest Element in Sorted Matrix
- LC 692: Top K Frequent Words

---

### 1️⃣3️⃣ K-way Merge
**When to use:** Merging K sorted lists/arrays

**Template:**
```python
import heapq

def merge_k_sorted(lists):
    heap = []
    
    # Add first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    result = []
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result
```

**LeetCode Problems:**
- LC 23: Merge K Sorted Lists
- LC 378: Kth Smallest Element in Sorted Matrix
- LC 373: Find K Pairs with Smallest Sums

---

### 1️⃣4️⃣ Dynamic Programming (0/1 Knapsack)
**When to use:** Optimization problems with choices

**Template:**
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],  # Don't take
                    values[i-1] + dp[i-1][w - weights[i-1]]  # Take
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

**LeetCode Problems:**
- LC 416: Partition Equal Subset Sum
- LC 494: Target Sum
- LC 322: Coin Change
- LC 518: Coin Change 2
- LC 1049: Last Stone Weight II

---

## 📚 How to Practice Patterns

### Week 1-2: Master 3 Patterns
1. Sliding Window
2. Two Pointers
3. Fast & Slow Pointers

### Week 3-4: Master 3 More
4. Merge Intervals
5. Cyclic Sort
6. In-place Reversal

### Week 5-6: Trees
7. Tree BFS
8. Tree DFS

### Week 7-8: Advanced
9. Two Heaps
10. Subsets
11. Modified Binary Search

### Week 9-10: Final Push
12. Top K Elements
13. K-way Merge
14. Dynamic Programming

## 🎯 Practice Strategy

1. **Learn the pattern**: Understand the template
2. **Solve 5-10 problems**: For each pattern
3. **Identify pattern**: When you see a new problem
4. **Apply template**: Modify for specific problem
5. **Optimize**: Improve time/space complexity

## 🏆 Pattern Recognition Tips

- **"Contiguous" subarray** → Sliding Window
- **Sorted array + pair** → Two Pointers
- **Linked List cycle** → Fast & Slow
- **Intervals/ranges** → Merge Intervals
- **Numbers in range [1,n]** → Cyclic Sort
- **Reverse linked list** → In-place Reversal
- **Tree level by level** → BFS
- **Tree paths** → DFS
- **Median/two halves** → Two Heaps
- **All combinations** → Subsets/Backtracking
- **Sorted + search** → Binary Search
- **K largest/smallest** → Heap/Top K
- **Multiple sorted arrays** → K-way Merge
- **Optimization with choices** → DP

---

**Master these 14 patterns and you'll be unstoppable on LeetCode!** 🚀
