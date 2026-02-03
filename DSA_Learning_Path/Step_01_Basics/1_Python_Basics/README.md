# Python Basics & Syntax for DSA

## 📌 Essential Python Concepts

This guide covers all Python concepts you need for solving DSA problems.

## 1. Input/Output

### Taking Input
```python
# Single integer
n = int(input())

# Single string
s = input()

# Multiple integers in one line
a, b = map(int, input().split())

# List of integers
arr = list(map(int, input().split()))

# Multiple lines
lines = []
for _ in range(n):
    lines.append(input())
```

### Printing Output
```python
# Basic print
print("Hello World")

# Print variables
print(n, s)

# Print with formatting
print(f"Value: {n}")

# Print without newline
print(n, end=" ")

# Print list elements
print(*arr)  # Unpacks list
```

## 2. Data Types

### Numbers
```python
# Integer
x = 10
# Float
y = 3.14
# Complex
z = 2 + 3j

# Type conversion
int_val = int(3.14)  # 3
float_val = float(5)  # 5.0
```

### Strings
```python
s = "Hello"

# Indexing
print(s[0])  # 'H'
print(s[-1])  # 'o'

# Slicing
print(s[0:3])  # 'Hel'
print(s[::-1])  # 'olleH' (reverse)

# Common methods
s.lower()
s.upper()
s.strip()
s.split()
s.replace('H', 'h')
s.count('l')
s.find('l')

# String concatenation
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
```

## 3. Operators

### Arithmetic
```python
a, b = 10, 3

print(a + b)   # 13 (Addition)
print(a - b)   # 7 (Subtraction)
print(a * b)   # 30 (Multiplication)
print(a / b)   # 3.333... (Division)
print(a // b)  # 3 (Floor Division)
print(a % b)   # 1 (Modulo)
print(a ** b)  # 1000 (Power)
```

### Comparison
```python
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater than or equal to
<=  # Less than or equal to
```

### Logical
```python
and  # Logical AND
or   # Logical OR
not  # Logical NOT
```

## 4. Conditionals

```python
# if-elif-else
if condition1:
    # code
elif condition2:
    # code
else:
    # code

# Ternary operator
result = value1 if condition else value2

# Example
n = 10
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## 5. Loops

### For Loop
```python
# Range
for i in range(5):  # 0 to 4
    print(i)

for i in range(1, 6):  # 1 to 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# Iterate over list
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num)

# Enumerate (with index)
for i, num in enumerate(arr):
    print(f"Index {i}: {num}")
```

### While Loop
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### Loop Control
```python
# break - exit loop
for i in range(10):
    if i == 5:
        break
    print(i)

# continue - skip iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Only odd numbers
```

## 6. Data Structures

### Lists (Most Used!)
```python
# Creation
arr = [1, 2, 3, 4, 5]
arr = []  # Empty list
arr = [0] * 5  # [0, 0, 0, 0, 0]

# Access
print(arr[0])   # First element
print(arr[-1])  # Last element
print(arr[1:4])  # Slicing

# Modification
arr[0] = 10
arr.append(6)       # Add at end
arr.insert(0, 0)    # Insert at index
arr.pop()           # Remove last
arr.pop(0)          # Remove at index
arr.remove(3)       # Remove first occurrence
arr.reverse()       # Reverse in-place
arr.sort()          # Sort in-place
arr.sort(reverse=True)  # Sort descending

# Common operations
len(arr)            # Length
max(arr)            # Maximum
min(arr)            # Minimum
sum(arr)            # Sum
arr.count(2)        # Count occurrences
arr.index(3)        # Find index

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

### Tuples (Immutable)
```python
t = (1, 2, 3)
# Cannot modify tuples
# Use for fixed data
```

### Sets (Unique elements, unordered)
```python
s = {1, 2, 3, 4, 5}
s = set()  # Empty set

s.add(6)        # Add element
s.remove(3)     # Remove element
s.discard(3)    # Remove if exists

# Set operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}
union = s1 | s2         # {1, 2, 3, 4, 5}
intersection = s1 & s2  # {3}
difference = s1 - s2    # {1, 2}
```

### Dictionaries (Hash Maps)
```python
# Creation
d = {'a': 1, 'b': 2, 'c': 3}
d = {}  # Empty dict
d = dict()

# Access
print(d['a'])      # 1
print(d.get('a'))  # 1
print(d.get('d', 0))  # 0 (default)

# Modification
d['a'] = 10     # Update
d['d'] = 4      # Add new
del d['a']      # Delete

# Iteration
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# Common operations
d.keys()        # All keys
d.values()      # All values
d.items()       # Key-value pairs
'a' in d        # Check if key exists
```

## 7. Functions

```python
# Basic function
def greet(name):
    return f"Hello {name}"

# Multiple parameters
def add(a, b):
    return a + b

# Default parameters
def power(base, exp=2):
    return base ** exp

# Multiple return values
def get_min_max(arr):
    return min(arr), max(arr)

# Variable arguments
def sum_all(*args):
    return sum(args)
```

## 8. Important Built-in Functions

```python
# Math
abs(-5)         # 5
pow(2, 3)       # 8
max(1, 2, 3)    # 3
min(1, 2, 3)    # 1
sum([1, 2, 3])  # 6
round(3.7)      # 4

# Type conversion
int(), float(), str(), list(), set(), tuple()

# Sorting
sorted([3, 1, 2])  # [1, 2, 3]
sorted([3, 1, 2], reverse=True)  # [3, 2, 1]

# Map, Filter
list(map(int, ['1', '2', '3']))  # [1, 2, 3]
list(filter(lambda x: x > 0, [-1, 0, 1, 2]))  # [1, 2]

# Zip
a = [1, 2, 3]
b = ['a', 'b', 'c']
list(zip(a, b))  # [(1, 'a'), (2, 'b'), (3, 'c')]

# Enumerate
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)  # 0 a, 1 b, 2 c

# Range
list(range(5))      # [0, 1, 2, 3, 4]
list(range(1, 5))   # [1, 2, 3, 4]
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]
```

## 9. Lambda Functions

```python
# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# With map
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))

# With filter
evens = list(filter(lambda x: x % 2 == 0, nums))

# Sorting with key
students = [('Alice', 85), ('Bob', 75), ('Charlie', 90)]
sorted_students = sorted(students, key=lambda x: x[1])
```

## 10. String Formatting

```python
name = "Alice"
age = 25

# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# format method
print("Name: {}, Age: {}".format(name, age))

# % operator
print("Name: %s, Age: %d" % (name, age))
```

## 🎯 Quick Practice Problems

Try these to test your understanding:

1. Read two numbers and print their sum
2. Check if a number is even or odd
3. Print first N natural numbers
4. Find the largest element in a list
5. Count frequency of each character in a string
6. Reverse a list
7. Check if a string is palindrome
8. Find sum of all even numbers in a list
9. Remove duplicates from a list
10. Merge two sorted lists

## ⚡ Pro Tips

1. **Use meaningful variable names**: `count` not `c`
2. **List comprehensions** are faster than loops for simple operations
3. **Use `in` operator** for membership testing
4. **Dict.get()** to avoid KeyError
5. **f-strings** for readable string formatting
6. **Negative indexing** for accessing from end: `arr[-1]`
7. **Slicing** is powerful: `arr[::-1]` reverses
8. **`//` for integer division**, not `int(a/b)`

---

**Practice these basics daily for 1 week to build muscle memory!**

Next: Move to Pattern Problems →
