class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Trường hợp loại ngay
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Với số chẵn: x == reversed_half
        # Với số lẻ: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
