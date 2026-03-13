# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or not k: return head
        
        cur, n = head, 1
        while cur.next:
            cur = cur.next
            n += 1
        
        k %= n
        if not k: return head
        
        cur.next = head  # nối thành vòng
        for _ in range(n - k):
            cur = cur.next
        
        head = cur.next
        cur.next = None
        return head
