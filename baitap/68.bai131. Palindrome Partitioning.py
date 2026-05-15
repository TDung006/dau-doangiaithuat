class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        path = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start):
            # Nếu đã đi hết chuỗi → lưu kết quả
            if start == len(s):
                result.append(path[:])
                return

            # Thử mọi cách cắt từ vị trí start
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if isPalindrome(sub):
                    path.append(sub)
                    backtrack(end)
                    path.pop()   # quay lui

        backtrack(0)
        return result
        