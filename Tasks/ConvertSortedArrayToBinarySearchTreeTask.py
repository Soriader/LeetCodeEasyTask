class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.branchHelper(nums, 0, len(nums) - 1)

    def branchHelper(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        node = TreeNode(nums[mid])

        node.left = self.branchHelper(nums, start, mid - 1)

        node.right = self.branchHelper(nums, mid + 1, end)

        return node

#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/