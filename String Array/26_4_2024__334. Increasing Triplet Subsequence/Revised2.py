class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        small = mid = float('inf')
        for i in nums:
            if i <= small:
                small=i
            elif small<i<=mid:
                mid = i
            elif i>mid:
                return True
        return False
