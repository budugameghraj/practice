# Step 3: Arrays

## 🎯 Overview

Arrays are the MOST IMPORTANT data structure in coding interviews. Master arrays, master interviews!

**Estimated Time**: 3-4 weeks

## 📚 Why Arrays?

- **Most common**: 40% of LeetCode problems use arrays
- **Foundation**: Needed for DP, Graphs, Trees
- **Interview staple**: Almost guaranteed in any interview

## 🎓 Array Topics

### 3.1 Easy Problems (15 problems)
Basic array manipulation and traversal:
- Largest element
- Second largest
- Check sorted
- Remove duplicates
- Rotate array
- Move zeros
- Linear search
- Find missing number
- Max consecutive ones
- Single number

### 3.2 Medium Problems (20 problems)
Two pointers, sliding window, and more:
- Two sum
- Sort 0s, 1s, 2s
- Majority element
- Maximum subarray sum (Kadane's)
- Rearrange array
- Next permutation
- Leaders in array
- Longest consecutive sequence
- Set matrix zeros
- Rotate matrix
- Spiral matrix

### 3.3 Hard Problems (10 problems)
Advanced techniques:
- Merge overlapping intervals
- Merge sorted arrays
- Find repeating and missing
- Inversion count
- Maximum product subarray
- Longest subarray with sum K

## 💡 Common Array Patterns

### 1. Two Pointers
```python
# Useful for sorted arrays, in-place modifications
left, right = 0, len(arr) - 1
while left < right:
    # process
    left += 1
    right -= 1
```

### 2. Sliding Window
```python
# For contiguous subarrays
window_start = 0
for window_end in range(len(arr)):
    # expand window
    while condition:
        # shrink window
        window_start += 1
```

### 3. Kadane's Algorithm
```python
# Maximum subarray sum
max_so_far = max_ending_here = arr[0]
for i in range(1, len(arr)):
    max_ending_here = max(arr[i], max_ending_here + arr[i])
    max_so_far = max(max_so_far, max_ending_here)
```

### 4. Hash Map for Frequency
```python
# Count frequencies
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
```

### 5. In-place Modification
```python
# Modify array without extra space
# Use index manipulation, swapping
```

## 🏆 Success Criteria

Complete Step 3 when you can:
- [ ] Solve Easy problems in < 15 minutes
- [ ] Solve Medium problems in < 30 minutes
- [ ] Identify pattern in new array problem
- [ ] Optimize for time and space complexity
- [ ] Explain your approach clearly

## 📖 Recommended Learning Path

### Week 1: Easy Problems
- Do 3-4 problems daily
- Focus on understanding logic
- Don't worry about optimization yet

### Week 2: Easy + Start Medium
- Complete remaining easy
- Start medium problems
- Learn two-pointer technique

### Week 3: Medium Problems
- 2-3 medium problems daily
- Learn Kadane's algorithm
- Practice sliding window

### Week 4: Hard Problems + Review
- 1-2 hard problems
- Review all previous problems
- Time yourself

## 🎯 LeetCode Mapping

Each problem folder contains:
- Problem description
- Hints
- Multiple solutions
- Complexity analysis
- LeetCode problem number

## ⚡ Pro Tips

1. **Master Easy first**: Don't rush to medium
2. **Draw it out**: Visualize array operations
3. **Edge cases**: Empty array, single element, all same
4. **Optimize later**: Working solution first
5. **Review patterns**: See the similarities

---

**Ready?** Start with `Easy/` folder!

**Next Step**: After Arrays, move to Step 4: Binary Search
