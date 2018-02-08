"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        path = ""
        res = []
        self.pathTree(root, path, res)
        return res

    def pathTree(self, root, path, res):
        if root is None:
            return
        path = path + str(root.val)
        if root.left:
            self.pathTree(root.left, path + '->', res)
        if root.right:
            self.pathTree(root.right, path + '->', res)
        if root.left is None and root.right is None:
            res.append(path)
