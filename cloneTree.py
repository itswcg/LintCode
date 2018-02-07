"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree
    @return: root of new tree
    """

    def cloneTree(self, root):
        if root:
            new = TreeNode(root.val)
        else:
            return
        new.left = self.cloneTree(root.left)
        new.right = self.cloneTree(root.right)
        return new
