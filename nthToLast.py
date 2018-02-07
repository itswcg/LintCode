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
    @return: Nth to last node of a singly linked list.
    """

    def nthToLast(self, head, n):
        cur = head
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            cur = cur.next
        return cur
