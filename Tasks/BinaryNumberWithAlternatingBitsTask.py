def hasAlternatingBits(self, n: int) -> bool:

    num_to_bin = bin(n)[2:]

    for i in range(len(num_to_bin) - 1):
        if num_to_bin[i] == num_to_bin[i + 1]:
            return False

    return True

#https://leetcode.com/problems/binary-number-with-alternating-bits/description/?envType=daily-question&envId=2026-02-18