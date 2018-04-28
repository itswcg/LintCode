# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        while pHead:
            tmp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = tmp
        return pre
