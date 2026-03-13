# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []
        
        def build(l, r):
            if l > r:
                return [None]
            
            res = []
            for i in range(l, r + 1):
                lefts = build(l, i - 1)
                rights = build(i + 1, r)
                for L in lefts:
                    for R in rights:
                        root = TreeNode(i)
                        root.left = L
                        root.right = R
                        res.append(root)
            return res
        
        return build(1, n)
        