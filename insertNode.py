"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if root:
            self._insert(node, root)
        else:
            root = node
        return root

    def _insert(self, node, root):
        if node.val < root.val:
            if root.left is not None:
                self._insert(node, root.left)
            else:
                root.left = node
        else:
            if root.right is not None:
                self._insert(node, root.right)
            else:
                root.right = node
