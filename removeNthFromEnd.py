"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        pre = ListNode(-1)
        pre.next = head
        p = pre
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            p = p.next
        p.next = p.next.next
        return pre.next
