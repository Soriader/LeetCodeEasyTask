def isPalindrome(self, s: str) -> bool:

    result = [ch.lower() for ch in s if ch.isalnum()]
    return result == result[::-1]

#https://leetcode.com/problems/valid-palindrome/