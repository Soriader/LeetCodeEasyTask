def plusOne(self, digits):

    number = int(''.join(str(digit) for digit in digits))
    new_number = number + 1
    new_number = str(new_number)
    result = []

    for digit in new_number:
        result.append(int(digit))

    return result

#https://leetcode.com/problems/plus-one/description/