def toHex(self, num):
    if num == 0:
        return "0"

    if num < 0:
        num = (1 << 32) + num

    hex_digits = "0123456789abcdef"
    result = []

    while num > 0:
        digit = num & 0xf
        result.append(hex_digits[digit])
        num >>= 4

    return ''.join(reversed(result))

#https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/