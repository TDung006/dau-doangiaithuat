class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1 << n):      # từ 0 đến 2^n - 1
            res.append(i ^ (i >> 1))
        return res
        