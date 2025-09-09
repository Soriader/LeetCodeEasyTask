import random

def firstBadVersion(self, n):

    left, right = 1, n

    while left < right:
        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left

def isBadVersion(version):
    return random.choice([True, False])
#This method is created for no error in compilation. This method is not available in this task so i created this simple version

#https://leetcode.com/problems/first-bad-version/description/