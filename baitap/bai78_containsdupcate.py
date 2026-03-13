class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path):
            # Add the current subset
            result.append(path[:])
            
            # Explore further elements
            for i in range(start, len(nums)):
                path.append(nums[i])          # include nums[i]
                backtrack(i + 1, path)        # recurse
                path.pop()                    # backtrack
        
        backtrack(0, [])
        return result
