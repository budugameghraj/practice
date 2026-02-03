# Step 16: Dynamic Programming (DP)

## 🎯 The Most Important Step!

Dynamic Programming is THE GAME CHANGER in coding interviews. Master DP, crack Google/Facebook!

**Estimated Time**: 6-8 weeks (don't rush this!)

## 📚 What is Dynamic Programming?

DP is an optimization technique that solves complex problems by:
1. **Breaking into subproblems**: Divide the problem
2. **Storing results**: Avoid recomputation (Memoization)
3. **Building solution**: Combine subproblem results

> "Those who cannot remember the past are condemned to repeat it." - George Santayana
> (This is literally what DP prevents!)

## 🎓 DP Fundamentals

### Two Approaches:

#### 1. Memoization (Top-Down)
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

#### 2. Tabulation (Bottom-Up)
```python
def fib_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

## 📖 DP Sub-Topics (9 Categories)

### 16.1: Introduction to DP
- What is DP?
- Fibonacci (the classic example)
- Climbing stairs
- House robber

### 16.2: 1D DP
- Climbing stairs variations
- Min cost climbing stairs
- House robber I & II
- Jump game

### 16.3: 2D/3D DP and DP on Grids
- Unique paths
- Unique paths II (with obstacles)
- Minimum path sum
- Triangle
- Maximal square

### 16.4: DP on Subsequences
- Subset sum
- Partition equal subset sum
- Count subsets with sum K
- Target sum

### 16.5: DP on Strings
- Longest common subsequence (LCS)
- Longest palindromic subsequence
- Edit distance
- Distinct subsequences
- Wildcard matching

### 16.6: DP on Stocks
- Best time to buy/sell stock (all variations I-VI)
- Stock problems are a pattern!

### 16.7: DP on LIS (Longest Increasing Subsequence)
- LIS basic
- Printing LIS
- Number of LIS
- Longest bitonic subsequence

### 16.8: MCM (Matrix Chain Multiplication) DP
- Matrix chain multiplication
- Palindrome partitioning
- Burst balloons
- Evaluate boolean expression

### 16.9: DP on Partitions
- Partition with given difference
- Count partitions with difference
- Partition array for maximum sum

## 💡 How to Identify DP Problems?

### Keywords to Look For:
- "Maximum/Minimum"
- "Count ways"
- "Optimize"
- "Find all possible"
- "Longest/Shortest"

### Classic Indicators:
1. Overlapping subproblems
2. Optimal substructure
3. Choices at each step
4. Count or optimize something

## 🎯 The DP Pattern (6 Steps)

### Step 1: Express in terms of index
What does dp[i] or dp[i][j] represent?

### Step 2: Try all choices
At each index, what are all possible choices?

### Step 3: Take min/max/sum
Based on problem, take optimal choice.

### Step 4: Base cases
When does recursion stop?

### Step 5: Memoization
Add memo to recursive solution.

### Step 6: Tabulation
Convert to iterative with table.

## 📝 Example: Fibonacci

### Step 1: Express
```
f(n) = nth fibonacci number
```

### Step 2: Choices
```
f(n) = f(n-1) + f(n-2)
```

### Step 3: Operation
```
Addition (sum of two previous)
```

### Step 4: Base Case
```
f(0) = 0, f(1) = 1
```

### Step 5: Memoization
```python
def fib(n, memo):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

### Step 6: Tabulation
```python
def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

## 🏆 Classic DP Problems (Must Solve)

### Beginner Level:
1. ✅ Fibonacci Number (LC 509)
2. ✅ Climbing Stairs (LC 70)
3. ✅ House Robber (LC 198)
4. ✅ Min Cost Climbing Stairs (LC 746)

### Intermediate Level:
5. ✅ Unique Paths (LC 62)
6. ✅ Minimum Path Sum (LC 64)
7. ✅ Longest Common Subsequence (LC 1143)
8. ✅ 0/1 Knapsack (Classic)
9. ✅ Coin Change (LC 322)
10. ✅ Longest Increasing Subsequence (LC 300)

### Advanced Level:
11. ✅ Edit Distance (LC 72)
12. ✅ Best Time to Buy/Sell Stock III (LC 123)
13. ✅ Burst Balloons (LC 312)
14. ✅ Regular Expression Matching (LC 10)
15. ✅ Wildcard Matching (LC 44)

## 🎓 Learning Path (8 Weeks)

### Week 1: Basics
- Understand memoization vs tabulation
- Solve: Fibonacci, Climbing Stairs
- Practice: 3-4 basic problems

### Week 2: 1D DP
- Linear DP problems
- House Robber variations
- Jump Game problems

### Week 3: 2D DP - Grids
- Unique Paths
- Minimum Path Sum
- Grid-based problems

### Week 4: Subsequences
- Subset sum problems
- Partition problems
- 0/1 Knapsack pattern

### Week 5: Strings
- LCS and variations
- Edit distance
- String matching

### Week 6: LIS Pattern
- Longest Increasing Subsequence
- Applications of LIS
- Binary search optimization

### Week 7: Stocks & MCM
- Stock problems (all 6)
- Matrix Chain Multiplication
- Partition DP

### Week 8: Practice & Review
- Mixed problems
- Time yourself
- Review difficult ones

## 💪 DP Templates

### Template 1: 0/1 Knapsack
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item
            dp[i][w] = dp[i-1][w]
            
            # Take item (if possible)
            if weights[i-1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    values[i-1] + dp[i-1][w - weights[i-1]]
                )
    
    return dp[n][capacity]
```

### Template 2: Longest Common Subsequence
```python
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

### Template 3: Grid Path
```python
def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    
    # Base case
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    
    # Fill table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]
```

## ⚡ Optimization Techniques

### 1. Space Optimization
Reduce 2D DP to 1D when only previous row is needed.

```python
# Instead of dp[i][j], use two arrays
prev = [0] * n
curr = [0] * n
```

### 2. State Reduction
Sometimes you can reduce number of states.

### 3. Binary Search on DP
For LIS, use binary search to optimize to O(n log n).

## 🚫 Common Mistakes

1. ❌ Not identifying it's a DP problem
2. ❌ Wrong state definition
3. ❌ Missing base cases
4. ❌ Wrong recurrence relation
5. ❌ Not optimizing space

## 🎯 Success Criteria

Master DP when you can:
- [ ] Identify DP problems in 30 seconds
- [ ] Write memoization solution quickly
- [ ] Convert to tabulation
- [ ] Optimize space complexity
- [ ] Solve medium DP in < 30 minutes
- [ ] Explain your approach clearly

## 📚 Resources

- **Striver's DP Playlist**: Complete 50+ problems
- **LeetCode DP Tag**: Practice extensively
- **This folder**: Organized by pattern

---

**DP is HARD but SO WORTH IT!**

Take your time, practice daily, and you'll master it! 💪

**Start here**: Introduction folder →
