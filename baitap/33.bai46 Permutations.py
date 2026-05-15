class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        result = []
        
        def backtrack(path, used):
            # If permutation is complete
            if len(path) == len(nums):
                result.append(path[:])  # make a copy
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # Choose
                used[i] = True
                path.append(nums[i])
                
                # Explore
                backtrack(path, used)
                
                # Un-choose (Backtrack)
                path.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return result
 