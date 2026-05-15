#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        norder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            # Pick current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Build left and right subtrees
            index = inorder_index[root_val]
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)