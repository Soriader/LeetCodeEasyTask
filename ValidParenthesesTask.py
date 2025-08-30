def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    mapping = {')': '(', ']': '[', '}': '{'}

    stack = []

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack:
                return False

            last = stack.pop()

            if last != mapping[char]:
                return False

    return len(stack) == 0

#https://leetcode.com/problems/valid-parentheses/description/
