class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def backtrack(s, open_cnt, close_cnt):
            # Nếu đủ 2*n ký tự → lưu kết quả
            if len(s) == 2 * n:
                res.append(s)
                return
            
            # Thêm "(" nếu còn quyền mở
            if open_cnt < n:
                backtrack(s + "(", open_cnt + 1, close_cnt)
            
            # Thêm ")" nếu không làm chuỗi sai
            if close_cnt < open_cnt:
                backtrack(s + ")", open_cnt, close_cnt + 1)

        backtrack("", 0, 0)
        return res
