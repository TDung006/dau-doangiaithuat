class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            
            while head:
                # Connect left → right
                head.left.next = head.right
                
                # Connect right → next subtree
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            
            leftmost = leftmost.left
        
        return root
