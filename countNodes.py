"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: the first node of linked list.
    @return: An integer
    """

    def countNodes(self, head):
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
