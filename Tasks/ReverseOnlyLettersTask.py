def reverseOnlyLetters(self, s):
    """
    :type s: str
    :rtype: str
    """
    reverse_s = ""

    for i in s:
        if i.isalpha():
            reverse_s += i

    reverse_s = reverse_s[::-1]

    result = []
    iterator = 0

    for letter in s:
        if letter.isalpha():
            result.append(reverse_s[iterator])
            iterator += 1
        else:
            result.append(letter)

    s = "".join(result)

    return s

#https://leetcode.com/problems/reverse-only-letters/description/