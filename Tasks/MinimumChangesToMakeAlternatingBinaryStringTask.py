def minOperations(self, s: str) -> int:
    iterator = 0

    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                iterator += 1
        else:
            if s[i] != '1':
                iterator += 1

    return min(iterator, len(s) - iterator)

#https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2026-03-05