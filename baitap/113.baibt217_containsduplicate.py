class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ds = []
        
        def Tohop(start, s, a):
            # Nếu đã chọn đủ k số
            if len(s) == k:
                if  a== n:
                    ds.append(s[:])
                return
            
            # Duyệt các số từ start đến 9
            for num in range(start, 10):
                # Nếu tổng vượt n thì dừng sớm
                if a + num > n:
                    break
                
                s.append(num)
                Tohop(num + 1, s, a+ num)
                s.pop()
        
        Tohop(1, [], 0)
        return ds