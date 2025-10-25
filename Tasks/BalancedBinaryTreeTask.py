class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def isBalanced(root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def check_root(node):
            if not node:
                return 0, True

            left_height, left_balanced = check_root(node.left)
            right_height, right_balanced = check_root(node.right)

            current_height = 1 + max(left_height, right_height)
            is_balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced

            return current_height, is_balanced

        return check_root(root)[1]

#https://leetcode.com/problems/balanced-binary-tree/description/