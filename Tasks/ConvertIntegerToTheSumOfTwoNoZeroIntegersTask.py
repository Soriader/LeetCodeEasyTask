def getNoZeroIntegers(self, n):
    a = 1
    while a < n:
        b = n - a
        if '0' not in str(a) and '0' not in str(b):
            return [a, b]
        a += 1

    return [1, n - 1]

#https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/?envType=daily-question&envId=2025-09-08