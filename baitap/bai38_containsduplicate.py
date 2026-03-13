class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"  # countAndSay(1)

        for _ in range(2, n + 1):
            result = ""
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    result += str(count) + s[i - 1]
                    count = 1

            # thêm nhóm cuối cùng
            result += str(count) + s[-1]
            s = result

        return s
