def repeatedCharacter(self, s):
    """
    :type s: str
    :rtype: str
    """

    letter_count = {}
    result = ''

    for letter in s:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
            if letter_count[letter] == 2:
                result = letter
                break

    return result


def repeatedCharacter2(self, s):

    letter_count = []
    for letter in s:
        if letter_count.count(letter):
            return letter
        else:
            letter_count.append(letter)

#https://leetcode.com/problems/first-letter-to-appear-twice/description/