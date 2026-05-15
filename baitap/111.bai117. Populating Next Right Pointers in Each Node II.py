class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        curr = root
        
        while curr:
            dummy = Node(0)
            tail = dummy
            
            # Traverse current level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                curr = curr.next
            
            # Move to next level
            curr = dummy.next
        
        return root