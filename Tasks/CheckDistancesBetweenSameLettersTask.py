from collections import Counter

def checkDistances(s, distance):
    """
    :type s: str
    :type distance: List[int]
    :rtype: bool
    """

    result = {}

    new_s = lettersThatAreTwice(s)

    for i in range(len(new_s)):
        letter = new_s[i]
        for j in range(i + 1, len(new_s)):
            if new_s[j] == letter:
                iterator = j - i - 1
                result[letter] = iterator
                break


    return result == correctDict(new_s, distance)


def correctDict(new_s, distance):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict_for_letters = {}

    for letter in alphabet:

        if letter in new_s:
            dict_for_letters.setdefault(letter, distance[alphabet.index(letter)])

    return dict_for_letters


def lettersThatAreTwice(s):

    count_letter = Counter(s)
    print("count_letter:", count_letter)

    result = ""

    for letter in s:

        if count_letter[letter] == 2:
            result += letter

    return result

#https://leetcode.com/problems/check-distances-between-same-letters/description/