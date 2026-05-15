class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
 
        m = [[0]*n for _ in range(n)]
        l, r, t, b, num = 0, n-1, 0, n-1, 1
        
        while l <= r and t <= b:
            for i in range(l, r+1): m[t][i] = num; num += 1
            t += 1
            for i in range(t, b+1): m[i][r] = num; num += 1
            r -= 1
            for i in range(r, l-1, -1): m[b][i] = num; num += 1
            b -= 1
            for i in range(b, t-1, -1): m[i][l] = num; num += 1
            l += 1
        
        return m
      