class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def backtrack(start, path):
            # đủ 4 phần
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            
            # thử đoạn dài 1 → 3
            for l in range(1, 4):
                if start + l > len(s):
                    break
                part = s[start:start + l]
                
                # không cho số 0 đứng đầu
                if part[0] == '0' and l > 1:
                    continue
                if int(part) <= 255:
                    backtrack(start + l, path + [part])

        backtrack(0, [])
        return res

        