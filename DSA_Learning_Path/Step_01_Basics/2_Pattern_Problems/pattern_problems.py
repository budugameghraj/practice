"""
Pattern Problems - Practice

Complete these 22 pattern problems to master nested loops!

Instructions:
1. Try each pattern yourself for at least 10 minutes
2. Draw it on paper first to understand the logic
3. Identify: rows, columns per row, what to print
4. Code it up!
5. Check pattern_solutions.py only if really stuck

Run: python3 pattern_problems.py
"""

def pattern_1(n):
    """
    Pattern 1: Square of Stars
    
    Input: n = 4
    Output:
    ****
    ****
    ****
    ****
    
    Hint: n rows, n stars per row
    """
    # TODO: Implement
    pass


def pattern_2(n):
    """
    Pattern 2: Right Triangle (Stars)
    
    Input: n = 5
    Output:
    *
    **
    ***
    ****
    *****
    
    Hint: Row i has i stars
    """
    # TODO: Implement
    pass


def pattern_3(n):
    """
    Pattern 3: Right Triangle (Numbers)
    
    Input: n = 5
    Output:
    1
    12
    123
    1234
    12345
    
    Hint: Row i prints numbers from 1 to i
    """
    # TODO: Implement
    pass


def pattern_4(n):
    """
    Pattern 4: Right Triangle (Same Number)
    
    Input: n = 5
    Output:
    1
    22
    333
    4444
    55555
    
    Hint: Row i prints i repeated i times
    """
    # TODO: Implement
    pass


def pattern_5(n):
    """
    Pattern 5: Inverted Right Triangle
    
    Input: n = 5
    Output:
    *****
    ****
    ***
    **
    *
    
    Hint: Row i has (n-i+1) stars
    """
    # TODO: Implement
    pass


def pattern_6(n):
    """
    Pattern 6: Inverted Number Triangle
    
    Input: n = 5
    Output:
    12345
    1234
    123
    12
    1
    
    Hint: Row i prints numbers from 1 to (n-i+1)
    """
    # TODO: Implement
    pass


def pattern_7(n):
    """
    Pattern 7: Star Pyramid
    
    Input: n = 5
    Output:
        *
       ***
      *****
     *******
    *********
    
    Hint: Row i has (n-i) spaces, then (2*i-1) stars
    """
    # TODO: Implement
    pass


def pattern_8(n):
    """
    Pattern 8: Inverted Star Pyramid
    
    Input: n = 5
    Output:
    *********
     *******
      *****
       ***
        *
    
    Hint: Row i has (i-1) spaces, then (2*(n-i+1)-1) stars
    """
    # TODO: Implement
    pass


def pattern_9(n):
    """
    Pattern 9: Diamond Pattern
    
    Input: n = 5
    Output:
        *
       ***
      *****
     *******
    *********
    *********
     *******
      *****
       ***
        *
    
    Hint: Combine patterns 7 and 8
    """
    # TODO: Implement
    pass


def pattern_10(n):
    """
    Pattern 10: Half Diamond
    
    Input: n = 5
    Output:
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    
    Hint: Increasing then decreasing stars
    """
    # TODO: Implement
    pass


def pattern_11(n):
    """
    Pattern 11: Binary Number Triangle
    
    Input: n = 5
    Output:
    1
    01
    101
    0101
    10101
    
    Hint: Start with 1 if (i+j) is even, 0 if odd
    """
    # TODO: Implement
    pass


def pattern_12(n):
    """
    Pattern 12: Number Crown
    
    Input: n = 4
    Output:
    1      1
    12    12
    123  123
    12341234
    
    Hint: Numbers, spaces (2*(n-i)), numbers again
    """
    # TODO: Implement
    pass


def pattern_13(n):
    """
    Pattern 13: Sequential Numbers Triangle
    
    Input: n = 5
    Output:
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
    
    Hint: Use a counter variable
    """
    # TODO: Implement
    pass


def pattern_14(n):
    """
    Pattern 14: Alphabet Triangle
    
    Input: n = 5
    Output:
    A
    AB
    ABC
    ABCD
    ABCDE
    
    Hint: Use chr(ord('A') + j)
    """
    # TODO: Implement
    pass


def pattern_15(n):
    """
    Pattern 15: Reverse Alphabet Triangle
    
    Input: n = 5
    Output:
    ABCDE
    ABCD
    ABC
    AB
    A
    
    Hint: Row i has (n-i+1) letters
    """
    # TODO: Implement
    pass


def pattern_16(n):
    """
    Pattern 16: Alphabet Repeat Pattern
    
    Input: n = 5
    Output:
    A
    BB
    CCC
    DDDD
    EEEEE
    
    Hint: Row i prints (i-th letter) i times
    """
    # TODO: Implement
    pass


def pattern_17(n):
    """
    Pattern 17: Alphabet Pyramid
    
    Input: n = 5
    Output:
        A
       ABA
      ABCBA
     ABCDCBA
    ABCDEDCBA
    
    Hint: Letters increase then decrease
    """
    # TODO: Implement
    pass


def pattern_18(n):
    """
    Pattern 18: Alphabet Triangle (Reverse Order)
    
    Input: n = 5
    Output:
    E
    ED
    EDC
    EDCB
    EDCBA
    
    Hint: Start from (n-th letter), go backwards
    """
    # TODO: Implement
    pass


def pattern_19(n):
    """
    Pattern 19: Hollow Square
    
    Input: n = 5
    Output:
    *****
    *   *
    *   *
    *   *
    *****
    
    Hint: Print * only at borders
    """
    # TODO: Implement
    pass


def pattern_20(n):
    """
    Pattern 20: Hollow Diamond
    
    Input: n = 5
    Output:
        *
       * *
      *   *
     *     *
    *       *
     *     *
      *   *
       * *
        *
    
    Hint: Print * only at edges of diamond
    """
    # TODO: Implement
    pass


def pattern_21(n):
    """
    Pattern 21: Butterfly Pattern
    
    Input: n = 5
    Output:
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    
    Hint: Stars, spaces, stars (symmetric)
    """
    # TODO: Implement
    pass


def pattern_22(n):
    """
    Pattern 22: Number Square Border
    
    Input: n = 4
    Output:
    4444444
    4333334
    4322234
    4321234
    4322234
    4333334
    4444444
    
    Hint: Value = n - min(distance from edges)
    This is HARD! Take your time.
    """
    # TODO: Implement
    pass


# ==================== MAIN ====================

def main():
    """
    Test your patterns here!
    """
    n = 5
    
    print("=== Pattern 1: Square ===")
    pattern_1(n)
    
    print("\n=== Pattern 2: Right Triangle ===")
    pattern_2(n)
    
    # Add more pattern calls as you complete them
    # print("\n=== Pattern 3: ... ===")
    # pattern_3(n)
    
    print("\nComplete all 22 patterns!")
    print("Check pattern_solutions.py if stuck!")


if __name__ == "__main__":
    main()
