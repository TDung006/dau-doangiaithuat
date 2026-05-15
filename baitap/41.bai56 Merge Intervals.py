class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
 
        intervals.sort()
        res = []
        for s, e in intervals:
            if not res or res[-1][1] < s:
                res.append([s, e])
            else:
                res[-1][1] = max(res[-1][1], e)
        return res
       