# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # sorted list
        
        cur = head
        while cur:
            prev = dummy
            
            # find position to insert
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            
            # save next node
            next_temp = cur.next
            
            # insert cur between prev and prev.next
            cur.next = prev.next
            prev.next = cur
            
            # move to next node
            cur = next_temp
        
        return dummy.next