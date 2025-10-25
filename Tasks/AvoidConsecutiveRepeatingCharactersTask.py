def modifyString(s):
    """
    :type s: str
    :rtype: str
    """
    s = list(s)
    n = len(s)

    for i in range(n):
        if s[i] == '?':
            left = s[i - 1] if i > 0 else ''
            right = s[i + 1] if i < n - 1 else ''

            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char != left and char != right:
                    s[i] = char
                    break

    return ''.join(s)


#https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/description/