# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        return self.subTree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def subTree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.subTree(A.left, B.left) and self.subTree(A.right, B.right)
