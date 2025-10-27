def sumOfEncryptedInt(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for num in nums:
        encrypt_number = createEncryptedInt(num)
        result += encrypt_number

    return result

def createEncryptedInt(nums):

    list_of_numbers = list(str(nums))
    return int(str(max(list_of_numbers)) * len(list_of_numbers))

#https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/