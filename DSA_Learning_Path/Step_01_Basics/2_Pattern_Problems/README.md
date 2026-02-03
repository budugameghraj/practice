# Pattern Problems

## 🎯 Why Pattern Problems?

Pattern problems are CRUCIAL for:
1. **Building loop logic**: Master nested loops
2. **Thinking systematically**: Break complex problems into simple steps
3. **Interview warmup**: Common in screening rounds
4. **Building confidence**: Easy wins to start your day

## 📚 Pattern Categories

### Category 1: Square Patterns
- Solid square
- Hollow square
- Square with diagonals

### Category 2: Triangle Patterns
- Right triangle (numbers)
- Right triangle (stars)
- Inverted triangle
- Pyramid

### Category 3: Number Patterns
- Sequential numbers
- Repeated numbers
- Number pyramids

### Category 4: Character Patterns
- Alphabet pyramids
- Character sequences

### Category 5: Special Patterns
- Diamond
- Butterfly
- Floyd's Triangle
- Pascal's Triangle

## 🎓 How to Approach Pattern Problems

### Step-by-Step Method:

1. **Identify rows**: How many rows? (usually = n)
2. **Identify columns per row**: Fixed or variable?
3. **Find the pattern**: What to print in each position?
4. **Code the logic**: 
   - Outer loop for rows
   - Inner loop(s) for columns
   - Print logic

### Example Breakdown:

**Problem**: Print a right triangle with stars
```
*
**
***
****
*****
```

**Analysis**:
- Rows: 5 (i from 1 to 5)
- Columns in row i: i stars
- Pattern: Print star i times in row i

**Code**:
```python
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()
```

## 💡 Common Loop Patterns

### Pattern 1: i iterations in row i
```python
for i in range(1, n + 1):
    for j in range(i):  # j from 0 to i-1
        print('*', end='')
    print()
```

### Pattern 2: Decreasing iterations
```python
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
```

### Pattern 3: Spaces + Stars (Pyramid)
```python
for i in range(1, n + 1):
    # Print spaces
    for j in range(n - i):
        print(' ', end='')
    # Print stars
    for j in range(2 * i - 1):
        print('*', end='')
    print()
```

## 🏆 Pro Tips

1. **Start simple**: Master basic patterns before complex ones
2. **Draw it out**: Visualize rows and columns on paper
3. **Use print statements**: Debug your loop counters
4. **Look for symmetry**: Many patterns have mirror properties
5. **Practice daily**: Do 2-3 patterns every day for a week

## 📝 Practice Problems (22 Total)

### Easy (1-10)
1. Square of stars
2. Right triangle
3. Inverted right triangle
4. Number pyramid
5. Number square
6. Reverse number triangle
7. Character pyramid
8. Repeated number pattern
9. Hollow square
10. Left-aligned triangle

### Medium (11-17)
11. Pyramid of stars
12. Inverted pyramid
13. Diamond pattern
14. Floyd's triangle
15. Number diamond
16. Butterfly pattern
17. Pascal's triangle (first 5 rows)

### Hard (18-22)
18. Hollow diamond
19. Number pattern with spaces
20. Zig-zag pattern
21. Alphabet diamond
22. Complex number pattern

## ⏰ Time Guidelines

- Easy patterns: 5-10 minutes each
- Medium patterns: 10-15 minutes each
- Hard patterns: 15-20 minutes each

## 🎯 Learning Outcomes

After completing all 22 patterns, you should be able to:
- [ ] Write nested loops confidently
- [ ] Solve any pattern problem in interview
- [ ] Understand row-column relationship
- [ ] Think in terms of iterations
- [ ] Debug loop logic effectively

---

**Ready to start?** Open `pattern_problems.py` and start coding!

**Stuck?** Check `pattern_solutions.py` (but try hard first!)
