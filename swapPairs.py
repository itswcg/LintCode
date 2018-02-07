"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @return: a ListNode
    """

    def swapPairs(self, head):
        p = head
        while p and p.next:
            tmp = p.val
            p.val = p.next.val
            p.next.val = tmp
            p = p.next.next
        return head
