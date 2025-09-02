def is_palindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False

    if x % 10 == 0 and x != 0:
        return False

    reversed_half = 0
    original = x

    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10

# Test
print(is_palindrome(121))    # True
print(is_palindrome(-121))   # False
print(is_palindrome(10))     # False

# https://leetcode.com/problems/palindrome-number/description/