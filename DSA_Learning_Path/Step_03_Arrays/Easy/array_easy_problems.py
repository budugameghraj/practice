"""
Array Easy Problems - Practice

These are fundamental array problems that appear frequently in interviews.
Each problem includes LeetCode reference for additional practice.

Complete these to build strong array manipulation skills!
"""

# ==================== PROBLEM 1 ====================
def find_largest(arr):
    """
    Find the largest element in the array.
    
    Example:
    Input: [3, 2, 1, 5, 4]
    Output: 5
    
    Example 2:
    Input: [10, 5, 8, 12, 3]
    Output: 12
    
    Constraints:
    - Array has at least one element
    - Elements can be negative
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    LeetCode: Related to LC 414 (Third Maximum Number)
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 2 ====================
def find_second_largest(arr):
    """
    Find the second largest element in the array.
    
    Example:
    Input: [12, 35, 1, 10, 34, 1]
    Output: 34
    
    Example 2:
    Input: [10, 5, 10]
    Output: 5
    
    Constraints:
    - Array has at least two unique elements
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Approach: Single pass, track largest and second_largest
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 3 ====================
def is_sorted(arr):
    """
    Check if array is sorted in ascending order.
    
    Example:
    Input: [1, 2, 3, 4, 5]
    Output: True
    
    Example 2:
    Input: [1, 3, 2, 4]
    Output: False
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 4 ====================
def remove_duplicates(arr):
    """
    Remove duplicates from sorted array in-place.
    Return length of array after removing duplicates.
    
    Example:
    Input: [1, 1, 2, 2, 3, 4, 4]
    Output: 4 (array becomes [1, 2, 3, 4, ...])
    
    Example 2:
    Input: [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Output: 5 (array becomes [0, 1, 2, 3, 4, ...])
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    LeetCode: LC 26 - Remove Duplicates from Sorted Array
    
    Hint: Use two pointers!
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 5 ====================
def rotate_array_left(arr, k):
    """
    Rotate array to the left by k positions.
    
    Example:
    Input: arr = [1, 2, 3, 4, 5], k = 2
    Output: [3, 4, 5, 1, 2]
    
    Example 2:
    Input: arr = [7, 8, 9, 10], k = 3
    Output: [10, 7, 8, 9]
    
    Time Complexity: O(n)
    Space Complexity: O(1) for optimal solution
    
    LeetCode: LC 189 - Rotate Array (rotate right)
    
    Hint: Use reversal algorithm
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 6 ====================
def move_zeros_to_end(arr):
    """
    Move all zeros to the end while maintaining order of non-zero elements.
    Modify array in-place.
    
    Example:
    Input: [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]
    
    Example 2:
    Input: [0, 0, 1]
    Output: [1, 0, 0]
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    LeetCode: LC 283 - Move Zeroes
    
    Hint: Two pointer approach - one for non-zero position
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 7 ====================
def linear_search(arr, target):
    """
    Find index of target element in array.
    Return -1 if not found.
    
    Example:
    Input: arr = [4, 2, 7, 1, 9], target = 7
    Output: 2
    
    Example 2:
    Input: arr = [1, 2, 3], target = 5
    Output: -1
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 8 ====================
def find_missing_number(arr, n):
    """
    Given array of size n-1 with numbers from 1 to n,
    find the missing number.
    
    Example:
    Input: arr = [1, 2, 4, 5], n = 5
    Output: 3
    
    Example 2:
    Input: arr = [1], n = 2
    Output: 2
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    LeetCode: LC 268 - Missing Number
    
    Hint: Use sum formula or XOR
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 9 ====================
def max_consecutive_ones(arr):
    """
    Find maximum number of consecutive 1s in binary array.
    
    Example:
    Input: [1, 1, 0, 1, 1, 1]
    Output: 3
    
    Example 2:
    Input: [1, 0, 1, 1, 0, 1]
    Output: 2
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    LeetCode: LC 485 - Max Consecutive Ones
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 10 ====================
def single_number(arr):
    """
    Every element appears twice except one. Find that single element.
    
    Example:
    Input: [2, 2, 1]
    Output: 1
    
    Example 2:
    Input: [4, 1, 2, 1, 2]
    Output: 4
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    LeetCode: LC 136 - Single Number
    
    Hint: Use XOR property - a ^ a = 0, a ^ 0 = a
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 11 ====================
def longest_subarray_with_sum_k(arr, k):
    """
    Find length of longest subarray with sum equal to k.
    (Array contains only positive numbers)
    
    Example:
    Input: arr = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3], k = 3
    Output: 3 (subarray [1, 1, 1])
    
    Example 2:
    Input: arr = [10, 5, 2, 7, 1, 9], k = 15
    Output: 4 (subarray [5, 2, 7, 1])
    
    Time Complexity: O(n) with sliding window
    Space Complexity: O(1)
    
    Hint: Use two pointers / sliding window
    """
    # TODO: Implement
    pass


# ==================== PROBLEM 12 ====================
def two_sum(arr, target):
    """
    Find two numbers that add up to target.
    Return indices of the two numbers.
    
    Example:
    Input: arr = [2, 7, 11, 15], target = 9
    Output: [0, 1] (because arr[0] + arr[1] = 9)
    
    Example 2:
    Input: arr = [3, 2, 4], target = 6
    Output: [1, 2]
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    LeetCode: LC 1 - Two Sum
    
    Hint: Use hash map to store complements
    """
    # TODO: Implement
    pass


# ==================== TEST CASES ====================

def run_tests():
    """Test all array problems"""
    
    print("Testing Problem 1: Find Largest")
    assert find_largest([3, 2, 1, 5, 4]) == 5
    assert find_largest([10, 5, 8, 12, 3]) == 12
    assert find_largest([-5, -2, -10]) == -2
    print("✓ Passed!\n")
    
    print("Testing Problem 2: Find Second Largest")
    assert find_second_largest([12, 35, 1, 10, 34, 1]) == 34
    assert find_second_largest([10, 5, 10]) == 5
    print("✓ Passed!\n")
    
    print("Testing Problem 3: Is Sorted")
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 3, 2, 4]) == False
    assert is_sorted([1, 1, 2, 2]) == True
    print("✓ Passed!\n")
    
    print("Testing Problem 4: Remove Duplicates")
    arr1 = [1, 1, 2, 2, 3, 4, 4]
    assert remove_duplicates(arr1) == 4
    arr2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(arr2) == 5
    print("✓ Passed!\n")
    
    print("Testing Problem 6: Move Zeros")
    arr = [0, 1, 0, 3, 12]
    move_zeros_to_end(arr)
    assert arr == [1, 3, 12, 0, 0]
    print("✓ Passed!\n")
    
    print("Testing Problem 7: Linear Search")
    assert linear_search([4, 2, 7, 1, 9], 7) == 2
    assert linear_search([1, 2, 3], 5) == -1
    print("✓ Passed!\n")
    
    print("Testing Problem 8: Missing Number")
    assert find_missing_number([1, 2, 4, 5], 5) == 3
    assert find_missing_number([1], 2) == 2
    print("✓ Passed!\n")
    
    print("Testing Problem 9: Max Consecutive Ones")
    assert max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3
    assert max_consecutive_ones([1, 0, 1, 1, 0, 1]) == 2
    print("✓ Passed!\n")
    
    print("Testing Problem 10: Single Number")
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    print("✓ Passed!\n")
    
    print("Testing Problem 12: Two Sum")
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("✓ Passed!\n")
    
    print("🎉 All tests passed!")


if __name__ == "__main__":
    # Uncomment to run tests when ready
    # run_tests()
    
    print("Complete all array problems above!")
    print("Then uncomment run_tests() to verify your solutions.")
