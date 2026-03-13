class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        n = len(nums)

        # khởi tạo bằng 3 số đầu
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                # cập nhật nếu gần target hơn
                if abs(s - target) < abs(closest - target):
                    closest = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s  # chính xác luôn

        return closest
