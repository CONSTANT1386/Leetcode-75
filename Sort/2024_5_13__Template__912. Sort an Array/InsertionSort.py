class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            currentVal = nums[i]
            j = i-1
            while j>=0 and nums[j]>=currentVal:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = currentVal
        return nums
