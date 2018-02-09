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
    @return: True if it has a cycle, or false
    """

    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        pre = head
        cur = head.next
        while cur.next and cur.next.next:
            if pre == cur:
                return True
            pre = pre.next
            cur = cur.next.next
        return False
