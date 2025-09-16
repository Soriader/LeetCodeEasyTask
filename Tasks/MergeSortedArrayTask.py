def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    nums1_position = m-1
    nums2_position = n-1
    current_position = m+n-1

    while nums1_position >= 0 and nums2_position >= 0:
        if nums1[nums1_position] < nums2[nums2_position]:
            nums1[current_position] = nums2[nums2_position]
            current_position -= 1
            nums2_position -= 1
        elif nums1[nums1_position] > nums2[nums2_position]:
            nums1[current_position] = nums1[nums1_position]
            current_position -= 1
            nums1_position -= 1
        else:
            nums1[current_position] = nums1[nums1_position]
            current_position -= 1
            nums1_position -= 1


    while nums1_position >= 0:
        nums1[current_position] = nums1[nums1_position]
        current_position -= 1
        nums1_position -= 1

    while nums2_position >= 0:
        nums1[current_position] = nums2[nums2_position]
        current_position -= 1
        nums2_position -= 1

#https://leetcode.com/problems/merge-sorted-array/description/
