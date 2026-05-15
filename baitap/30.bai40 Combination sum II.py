class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []

        def backtrack(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                # tránh trùng
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # cắt nhánh sớm
                if candidates[i] > remain:
                    break

                path.append(candidates[i])
                backtrack(i + 1, path, remain - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res

        