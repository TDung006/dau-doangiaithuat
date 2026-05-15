# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        size = getLength(head)
        self.curr = head
        
        # Step 2: build BST using inorder traversal
        def build(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # build left subtree
            left_child = build(left, mid - 1)
            
            # current list node becomes tree root
            root = TreeNode(self.curr.val)
            root.left = left_child
            
            self.curr = self.curr.next
            
            # build right subtree
            root.right = build(mid + 1, right)
            
            return root
        
        return build(0, size - 1)