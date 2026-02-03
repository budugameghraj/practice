"""
Python Basics - Practice Problems

Complete these 10 problems to master Python basics for DSA.
Each problem builds essential skills for coding interviews.

Test your solutions by running: python3 01_basic_problems.py
"""

# Problem 1: Sum of Two Numbers
# Time Complexity: O(1)
# Space Complexity: O(1)
def sum_two_numbers(a, b):
    """
    Given two integers a and b, return their sum.
    
    Example:
    Input: a = 5, b = 3
    Output: 8
    """
    # TODO: Implement this
    pass


# Problem 2: Check Even or Odd
# Time Complexity: O(1)
# Space Complexity: O(1)
def is_even(n):
    """
    Check if a number is even.
    
    Example:
    Input: 4
    Output: True
    
    Input: 7
    Output: False
    """
    # TODO: Implement this
    pass


# Problem 3: Find Maximum in List
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_max(arr):
    """
    Find the maximum element in the array.
    
    Example:
    Input: [3, 7, 2, 9, 1]
    Output: 9
    """
    # TODO: Implement this
    pass


# Problem 4: Count Frequency
# Time Complexity: O(n)
# Space Complexity: O(k) where k is number of unique elements
def count_frequency(arr):
    """
    Count frequency of each element in array.
    Return a dictionary with element as key and frequency as value.
    
    Example:
    Input: [1, 2, 2, 3, 3, 3]
    Output: {1: 1, 2: 2, 3: 3}
    """
    # TODO: Implement this
    pass


# Problem 5: Reverse a List
# Time Complexity: O(n)
# Space Complexity: O(1) for in-place, O(n) for new list
def reverse_list(arr):
    """
    Reverse the array and return it.
    
    Example:
    Input: [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]
    """
    # TODO: Implement this
    pass


# Problem 6: Check Palindrome String
# Time Complexity: O(n)
# Space Complexity: O(1)
def is_palindrome(s):
    """
    Check if string is a palindrome (reads same forwards and backwards).
    
    Example:
    Input: "racecar"
    Output: True
    
    Input: "hello"
    Output: False
    """
    # TODO: Implement this
    pass


# Problem 7: Sum of Even Numbers
# Time Complexity: O(n)
# Space Complexity: O(1)
def sum_of_evens(arr):
    """
    Return sum of all even numbers in the array.
    
    Example:
    Input: [1, 2, 3, 4, 5, 6]
    Output: 12 (2 + 4 + 6)
    """
    # TODO: Implement this
    pass


# Problem 8: Remove Duplicates
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates(arr):
    """
    Remove duplicates from array while maintaining order.
    
    Example:
    Input: [1, 2, 2, 3, 4, 4, 5]
    Output: [1, 2, 3, 4, 5]
    """
    # TODO: Implement this
    pass


# Problem 9: Character Frequency in String
# Time Complexity: O(n)
# Space Complexity: O(k) where k is unique characters
def char_frequency(s):
    """
    Count frequency of each character in string.
    
    Example:
    Input: "hello"
    Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # TODO: Implement this
    pass


# Problem 10: Merge Two Sorted Lists
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
def merge_sorted_lists(arr1, arr2):
    """
    Merge two sorted arrays into one sorted array.
    
    Example:
    Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
    Output: [1, 2, 3, 4, 5, 6]
    """
    # TODO: Implement this
    pass


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
    # Uncomment to run tests when you're ready
    # test_problems()
    
    print("Complete all 10 functions above, then uncomment test_problems() to verify!")
