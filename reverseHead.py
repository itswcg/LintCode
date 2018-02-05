"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        else:
            newhead = self.reverse(head.next)
            head.next.next = head
            head.next = None
        return newhead
