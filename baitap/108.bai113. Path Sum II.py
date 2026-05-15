# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        
        def dfs(node, remaining, path):
            if not node:
                return
            
            path.append(node.val)
            remaining -= node.val
            
            # If it's a leaf and sum matches
            if not node.left and not node.right and remaining == 0:
                result.append(list(path))  # copy path
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)
            
            path.pop()  # backtrack
        
        dfs(root, targetSum, [])
        return result
        