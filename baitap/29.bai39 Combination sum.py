class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    
        res = []

        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remain - candidates[i])  # i (không phải i+1)
                path.pop()

        backtrack(0, [], target)
        return res
