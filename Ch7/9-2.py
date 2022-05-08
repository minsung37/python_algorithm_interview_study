# https://leetcode.com/problems/3sum/
# 796ms 18.1MB - 세 수의 합(책풀이)
class Solution:
    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:
        result, length = [], len(nums)
        nums.sort()
        for i in range(length - 2):
            if nums[i] > 0 or (i > 0 and nums[i] == nums[i - 1]):
                continue
            left, right = i + 1, length - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left = left + 1
                elif three_sum > 0:
                    right = right - 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
        return result