class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for index, num in enumerate(nums):
            if index == 0 or index == len(nums) - 1:
                continue
            if num > min(nums[:index]) and num < max(nums[index+1:]):
                return True
        return False

  # Notice: this is time out!
