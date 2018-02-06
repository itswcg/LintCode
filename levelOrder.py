"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        res = []
        if root is None:
            return res
        q = [root]
        while len(q) != 0:
            tmp = []
            for i in range(len(q)):
                r = q.pop(0)
                if r.left is not None:
                    q.append(r.left)
                if r.right is not None:
                    q.append(r.right)
                tmp.append(r.val)
            res.append(tmp)
        return res
