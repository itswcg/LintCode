# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        res = []
        while head:
            res.append(head)
            head = head.next
        if k > len(res) or k < 1: return
        return res[-k]
