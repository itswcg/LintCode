class Solution:
    """
    @param: : the given tree
    @return: Whether it is a full tree
    """

    def isFullTree(self, root):
        if root is None:
            return True
        if root.left and root.right is None or root.right and root.left is None:
            return False
        return self.isFullTree(root.left) and self.isFullTree(root.right)
