# https://leetcode.com/problems/3sum-closest/
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target
        return closest
