"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        if root is None:
            return None
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))

    def max(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a.val > b.val:
            return a
        else:
            return b
