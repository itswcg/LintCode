"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):
        if head is None:
            return
        l = []
        self.sortedList(head, l)
        return self.buildTree(l, 0, len(l) - 1)

    def sortedList(self, head, l):
        while head:
            l.append(head.val)
            head = head.next

    def buildTree(self, A, start, end):
        if start > end:
            return
        mid = (start + end) // 2
        node = TreeNode(A[mid])
        node.left = self.buildTree(A, start, mid - 1)
        node.right = self.buildTree(A, mid + 1, end)
        return node
