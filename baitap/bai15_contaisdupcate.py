class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       
       
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # bỏ trùng cho số đầu tiên
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # bỏ trùng cho left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # bỏ trùng cho right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res
