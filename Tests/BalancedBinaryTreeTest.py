import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Tasks'))

from Tasks.BalancedBinaryTreeTask import isBalanced, TreeNode


class BalancedBinaryTreeTests(unittest.TestCase):

    def test_balanced_tree(self):
        #     3
        #    / \
        #   9  20
        #     /  \
        #    15   7
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertTrue(isBalanced(root))

    def test_unbalanced_tree(self):
        #     1
        #    / \
        #   2   2
        #  / \
        # 3   3
        # / \
        # 4   4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)

        self.assertFalse(isBalanced(root))

    def test_empty_tree(self):
        self.assertTrue(isBalanced(None))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(isBalanced(root))

    def test_left_heavy_unbalanced(self):
        #     1
        #    /
        #   2
        #  /
        # 3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)

        self.assertFalse(isBalanced(root))

    def test_right_heavy_unbalanced(self):
        #     1
        #      \
        #       2
        #        \
        #         3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        self.assertFalse(isBalanced(root))

    def test_complex_balanced(self):
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   5   6
        #  /
        # 7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.left.left.left = TreeNode(7)

        self.assertTrue(isBalanced(root))

    def test_complex_unbalanced(self):
        #       1
        #      / \
        #     2   3
        #    / \   \
        #   4   5   6
        #  / \
        # 7   8
        #      \
        #       9
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(8)
        root.left.left.right.right = TreeNode(9)

        self.assertFalse(isBalanced(root))

    def test_symmetric_balanced(self):
        #     1
        #    / \
        #   2   2
        #  / \ / \
        # 3  4 4  3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)

        self.assertTrue(isBalanced(root))

    def test_minimal_unbalanced(self):
        #   1
        #  / \
        # 2   3
        #    / \
        #   4   5
        #      /
        #     6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.right.left = TreeNode(6)

        self.assertFalse(isBalanced(root))


if __name__ == '__main__':
    unittest.main()