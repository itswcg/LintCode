"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return:
    """

    def flatten(self, root):
        l = []
        self.preOrder(root, l)
        p = root
        for i in range(1, len(l)):
            p1 = TreeNode(l[i])
            p.left = None
            p.right = p1
            p = p.right

    def preOrder(self, root, l):
        if root is None:
            return
        l.append(root.val)
        self.preOrder(root.left, l)
        self.preOrder(root.right, l)
