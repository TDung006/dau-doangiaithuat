# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
       
        dummy = ListNode(0)
        dummy.next = head

        fast = slow = dummy

        # fast đi trước n bước
        for _ in range(n):
            fast = fast.next

        # cùng đi đến cuối
        while fast.next:
            fast = fast.next
            slow = slow.next

        # xóa node thứ n từ cuối
        slow.next = slow.next.next

        return dummy.next
