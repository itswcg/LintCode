#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        if abs(self.depthTree(pRoot.left)-self.depthTree(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)


    def depthTree(self, root):
        if root is None:
            return 0
        return max(self.depthTree(root.left), self.depthTree(root.right)) + 1
