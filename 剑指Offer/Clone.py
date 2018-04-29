# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead: return pHead
        p = RandomListNode(pHead.label)
        p.next = pHead.next
        p.random = pHead.random
        p.next = self.Clone(pHead.next)
        return p
