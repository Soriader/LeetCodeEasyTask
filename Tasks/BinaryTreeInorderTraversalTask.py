class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorderTraversal(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """

    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result

#https://leetcode.com/problems/binary-tree-inorder-traversal/description/