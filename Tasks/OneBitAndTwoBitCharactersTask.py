def isOneBitCharacter(bits):
    index = 0

    while index < len(bits) - 1:
        if bits[index] == 1:
            index += 2
        else:
            index += 1

    return index == len(bits) - 1

#https://leetcode.com/problems/1-bit-and-2-bit-characters/description/?envType=daily-question&envId=2025-11-18