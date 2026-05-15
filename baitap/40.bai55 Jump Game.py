class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
 
        reach = 0
        for i, jump in enumerate(nums):
            if i > reach: return False
            reach = max(reach, i + jump)
        return True
      