"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        if root is None:
            return True
        return abs(self._height(root.left) - self._height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def _height(self, root):
        if root is None:
            return 0
        return max(self._height(root.left), self._height(root.right)) + 1
