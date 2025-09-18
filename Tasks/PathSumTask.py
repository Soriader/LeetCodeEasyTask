class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def dfs(root, current_sum):
            if not root:
                return False

            current_sum += root.val
            if not root.left and not root.right:
                return current_sum == targetSum

            return dfs(root.left, current_sum) or dfs(root.right, current_sum)

        return dfs(root,0)

#https://leetcode.com/problems/path-sum/description/