"""
Python Basics - Solutions

Here are the solutions to all 10 practice problems.
Try to solve them yourself first before looking at these!
"""

# Problem 1: Sum of Two Numbers
def sum_two_numbers(a, b):
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return a + b


# Problem 2: Check Even or Odd
def is_even(n):
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    
    Alternative: return n % 2 == 0
    """
    return n % 2 == 0


# Problem 3: Find Maximum in List
def find_max(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Method 1: Using built-in max()
    """
    return max(arr)
    
    # Method 2: Manual iteration
    # max_val = arr[0]
    # for num in arr:
    #     if num > max_val:
    #         max_val = num
    # return max_val


# Problem 4: Count Frequency
def count_frequency(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(k) where k is unique elements
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq
    
    # Alternative using Counter
    # from collections import Counter
    # return dict(Counter(arr))


# Problem 5: Reverse a List
def reverse_list(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(n) for new list, O(1) for in-place
    """
    # Method 1: Slicing (creates new list)
    return arr[::-1]
    
    # Method 2: reversed() function
    # return list(reversed(arr))
    
    # Method 3: In-place reversal
    # arr.reverse()
    # return arr
    
    # Method 4: Two pointers (in-place)
    # left, right = 0, len(arr) - 1
    # while left < right:
    #     arr[left], arr[right] = arr[right], arr[left]
    #     left += 1
    #     right -= 1
    # return arr


# Problem 6: Check Palindrome String
def is_palindrome(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Method 1: Using slicing
    return s == s[::-1]
    
    # Method 2: Two pointers
    # left, right = 0, len(s) - 1
    # while left < right:
    #     if s[left] != s[right]:
    #         return False
    #     left += 1
    #     right -= 1
    # return True


# Problem 7: Sum of Even Numbers
def sum_of_evens(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Method 1: Simple loop
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total
    
    # Method 2: Using filter and sum
    # return sum(filter(lambda x: x % 2 == 0, arr))
    
    # Method 3: List comprehension
    # return sum([x for x in arr if x % 2 == 0])


# Problem 8: Remove Duplicates
def remove_duplicates(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Method 1: Using dict to maintain order (Python 3.7+)
    result = []
    seen = set()
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result
    
    # Method 2: Using dict.fromkeys (maintains order in Python 3.7+)
    # return list(dict.fromkeys(arr))


# Problem 9: Character Frequency in String
def char_frequency(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(k) where k is unique characters
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq
    
    # Alternative using Counter
    # from collections import Counter
    # return dict(Counter(s))


# Problem 10: Merge Two Sorted Lists
def merge_sorted_lists(arr1, arr2):
    """
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    
    This is a classic two-pointer technique!
    """
    result = []
    i, j = 0, 0
    
    # Compare elements from both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    # Add remaining elements from arr2
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result
    
    # Alternative: Simple but less efficient O((n+m)log(n+m))
    # return sorted(arr1 + arr2)


# ==================== TEST CASES ====================

def test_problems():
    """Test all problems"""
    
    print("Testing Problem 1: Sum of Two Numbers")
    assert sum_two_numbers(5, 3) == 8
    assert sum_two_numbers(-1, 1) == 0
    assert sum_two_numbers(0, 0) == 0
    print("✓ All tests passed!\n")
    
    print("Testing Problem 2: Check Even or Odd")
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("✓ All tests passed!\n")
    
    print("Testing Problem 3: Find Maximum")
    assert find_max([3, 7, 2, 9, 1]) == 9
    assert find_max([1]) == 1
    assert find_max([-5, -2, -10]) == -2
    print("✓ All tests passed!\n")
    
    print("Testing Problem 4: Count Frequency")
    assert count_frequency([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert count_frequency([1, 1, 1, 1]) == {1: 4}
    print("✓ All tests passed!\n")
    
    print("Testing Problem 5: Reverse List")
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list([1]) == [1]
    print("✓ All tests passed!\n")
    
    print("Testing Problem 6: Check Palindrome")
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("a") == True
    print("✓ All tests passed!\n")
    
    print("Testing Problem 7: Sum of Evens")
    assert sum_of_evens([1, 2, 3, 4, 5, 6]) == 12
    assert sum_of_evens([1, 3, 5]) == 0
    print("✓ All tests passed!\n")
    
    print("Testing Problem 8: Remove Duplicates")
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates([1, 1, 1]) == [1]
    print("✓ All tests passed!\n")
    
    print("Testing Problem 9: Character Frequency")
    assert char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print("✓ All tests passed!\n")
    
    print("Testing Problem 10: Merge Sorted Lists")
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted_lists([], [1, 2]) == [1, 2]
    print("✓ All tests passed!\n")
    
    print("🎉 All problems solved correctly!")


if __name__ == "__main__":
    test_problems()
