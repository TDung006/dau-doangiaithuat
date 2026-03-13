class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in mapping:  # ngoặc đóng
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:  # ngoặc mở
                stack.append(ch)

        return not stack
