class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:return pHead
        pre = ListNode(0)
        pre.next = pHead
        p = pre
        cur = pHead
        while cur and cur.next:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
            else:
                p.next =cur
                p = p.next
            cur = cur.next
        p.next = cur
        return pre.next
