class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0:
            return right + 1
        elif right == 0:
            return left + 1

        return min(left, right) + 1

    #https://leetcode.com/problems/minimum-depth-of-binary-tree/description/