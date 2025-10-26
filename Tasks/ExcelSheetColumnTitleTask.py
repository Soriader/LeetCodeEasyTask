import string

def convertToTitle(columnNumber):
    num_to_letter = {i + 1: letter for i, letter in enumerate(string.ascii_uppercase)}

    result = ""

    while columnNumber > 0:
        remainder = columnNumber % 26
        if remainder == 0:
            remainder = 26
        result = num_to_letter[remainder] + result
        columnNumber = (columnNumber - remainder) // 26

    return result
#https://leetcode.com/problems/excel-sheet-column-title/description/