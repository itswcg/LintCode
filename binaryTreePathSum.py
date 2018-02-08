"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        path = []
        res = []
        self.pathTree(root, path, res, target)
        return res

    def pathTree(self, root, path, res, target):
        if root is None:
            return
        path = path + [root.val]
        if root.left:
            self.pathTree(root.left, path, res, target)
        if root.right:
            self.pathTree(root.right, path, res, target)
        if root.left is None and root.right is None and sum(path) == target:
            res.append(path)
