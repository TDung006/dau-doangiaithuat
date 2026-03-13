class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Nếu chuỗi rỗng sau khi bỏ space
        if i == n:
            return 0
        
        # 2. Check sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
            
            # 4. Handle overflow
            if sign * num <= INT_MIN:
                return INT_MIN
            if sign * num >= INT_MAX:
                return INT_MAX
            
            i += 1
        
        return sign * num