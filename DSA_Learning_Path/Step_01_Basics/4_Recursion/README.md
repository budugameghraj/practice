# Recursion Fundamentals

## 🎯 What is Recursion?

**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar sub-problems.

> "To understand recursion, you must first understand recursion." 😄

## 📚 Key Concepts

### 1. Base Case
The condition that stops the recursion (prevents infinite loop).

### 2. Recursive Case
The part where function calls itself with a smaller/simpler input.

### 3. Call Stack
Each recursive call is added to the call stack, and returns are processed in LIFO order.

## 🎓 Basic Template

```python
def recursive_function(parameters):
    # Base case - when to stop
    if base_condition:
        return base_value
    
    # Recursive case - call itself
    return recursive_function(modified_parameters)
```

## 💡 Simple Examples

### Example 1: Print N to 1

```python
def print_n_to_1(n):
    # Base case
    if n == 0:
        return
    
    # Print current number
    print(n)
    
    # Recursive call with n-1
    print_n_to_1(n - 1)

# Output for n=5: 5 4 3 2 1
```

**How it works:**
1. print_n_to_1(5) → prints 5, calls print_n_to_1(4)
2. print_n_to_1(4) → prints 4, calls print_n_to_1(3)
3. print_n_to_1(3) → prints 3, calls print_n_to_1(2)
4. print_n_to_1(2) → prints 2, calls print_n_to_1(1)
5. print_n_to_1(1) → prints 1, calls print_n_to_1(0)
6. print_n_to_1(0) → BASE CASE, returns

### Example 2: Print 1 to N

```python
def print_1_to_n(n):
    # Base case
    if n == 0:
        return
    
    # Recursive call FIRST
    print_1_to_n(n - 1)
    
    # Then print (after returning from recursion)
    print(n)

# Output for n=5: 1 2 3 4 5
```

**Key Insight:** Print AFTER recursive call to reverse order!

### Example 3: Factorial

```python
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
```

### Example 4: Sum of N Natural Numbers

```python
def sum_n(n):
    # Base case
    if n == 0:
        return 0
    
    # Recursive case: sum(n) = n + sum(n-1)
    return n + sum_n(n - 1)

# sum_n(5) = 5 + 4 + 3 + 2 + 1 = 15
```

## 🔍 Visualizing Recursion: Recursion Tree

For `factorial(4)`:
```
factorial(4)
    ↓
4 * factorial(3)
        ↓
    3 * factorial(2)
            ↓
        2 * factorial(1)
                ↓
            1 [BASE CASE]
            
Returns:
    1 → 2*1=2 → 3*2=6 → 4*6=24
```

## ⚡ Types of Recursion

### 1. Direct Recursion
Function calls itself directly.
```python
def func():
    func()  # Direct
```

### 2. Indirect Recursion
Function A calls B, B calls A.
```python
def func_a():
    func_b()

def func_b():
    func_a()
```

### 3. Tail Recursion
Recursive call is the last operation.
```python
def tail_recursive(n):
    if n == 0:
        return
    print(n)
    tail_recursive(n - 1)  # Last operation
```

### 4. Non-Tail Recursion
Operations after recursive call.
```python
def non_tail_recursive(n):
    if n == 0:
        return 1
    return n * non_tail_recursive(n - 1)  # Multiplication after call
```

## 🎯 Important Recursion Problems

### Problem 1: Fibonacci Number
```python
def fibonacci(n):
    """
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2)
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci(6) = 8
# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
```

### Problem 2: Reverse an Array
```python
def reverse_array(arr, start, end):
    """Reverse array using recursion"""
    if start >= end:
        return
    
    # Swap
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recursive call
    reverse_array(arr, start + 1, end - 1)
```

### Problem 3: Check Palindrome
```python
def is_palindrome(s, start, end):
    """Check if string is palindrome"""
    if start >= end:
        return True
    
    if s[start] != s[end]:
        return False
    
    return is_palindrome(s, start + 1, end - 1)
```

### Problem 4: Power Function
```python
def power(base, exp):
    """Calculate base^exp using recursion"""
    if exp == 0:
        return 1
    
    if exp < 0:
        return 1 / power(base, -exp)
    
    return base * power(base, exp - 1)

# Optimized version (divide and conquer):
def power_optimized(base, exp):
    if exp == 0:
        return 1
    
    half = power_optimized(base, exp // 2)
    
    if exp % 2 == 0:
        return half * half
    else:
        return base * half * half
```

## 💪 Multiple Recursive Calls

Some problems require multiple recursive calls:

### Fibonacci (2 calls)
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # 2 recursive calls!
```

### Tower of Hanoi (2 calls)
```python
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)
```

## 🚫 Common Mistakes

1. **Missing Base Case**: Causes infinite recursion
2. **Wrong Base Case**: Doesn't cover all edge cases
3. **Not Moving Towards Base Case**: Parameters don't change correctly
4. **Stack Overflow**: Too many recursive calls

## ⚙️ Time & Space Complexity

### Time Complexity:
- Depends on number of recursive calls
- Linear: O(n) for simple recursion (factorial, sum)
- Exponential: O(2^n) for multiple calls (fibonacci)

### Space Complexity:
- **O(recursion depth)** due to call stack
- For n recursive calls: O(n) space
- This is why very deep recursion can cause stack overflow

## 🎯 When to Use Recursion?

✅ **Good for:**
- Tree/Graph traversal
- Divide and conquer algorithms
- Backtracking problems
- Problems with recursive structure (factorial, fibonacci)
- When problem can be broken into similar sub-problems

❌ **Avoid when:**
- Simple iterative solution exists
- Very deep recursion (stack overflow risk)
- Performance is critical (recursion has overhead)

## 🔄 Recursion vs Iteration

| Recursion | Iteration |
|-----------|-----------|
| More elegant | More efficient |
| Natural for some problems | Better for simple loops |
| Uses call stack (space) | Uses less memory |
| Can cause stack overflow | No stack issues |
| Easier to understand | Requires loop logic |

## 📝 Practice Problems

Start with these 10 problems in `recursion_problems.py`:

1. Print N to 1
2. Print 1 to N  
3. Sum of first N numbers
4. Factorial
5. Fibonacci (nth number)
6. Power function
7. Reverse array
8. Check palindrome
9. Count digits
10. Sum of digits

## 🏆 Success Criteria

You've mastered recursion when you can:
- [ ] Write base case without thinking
- [ ] Draw recursion trees for any problem
- [ ] Convert simple loops to recursion
- [ ] Understand call stack behavior
- [ ] Calculate time/space complexity

## ⚠️ Important Notes

1. **Always define base case first** in your thinking
2. **Trust the recursion**: Don't try to trace every call
3. **Draw it out**: Recursion trees help immensely
4. **Practice daily**: Recursion needs muscle memory
5. **Start simple**: Master basics before complex problems

---

**Remember**: Recursion is one of the MOST IMPORTANT concepts in DSA. It's used in:
- Binary Trees
- Graphs
- Dynamic Programming
- Backtracking
- Divide and Conquer

**Master it now, thank yourself later!**

Next: Practice all problems in `recursion_problems.py` →
