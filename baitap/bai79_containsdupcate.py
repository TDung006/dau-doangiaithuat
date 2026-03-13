class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(b), len(b[0])
        def dfs(i, j, k):
            if k == len(w): return True
            if i<0 or j<0 or i>=m or j>=n or b[i][j]!=w[k]: return False
            b[i][j], t = '#', b[i][j]
            r = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            b[i][j] = t
            return r
        return any(dfs(i,j,0) for i in range(m) for j in range(n))