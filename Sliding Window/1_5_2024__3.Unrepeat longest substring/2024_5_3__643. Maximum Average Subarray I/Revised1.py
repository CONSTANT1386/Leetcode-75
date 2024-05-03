class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k,n):
            total = total + nums[i] - nums[i-k]
            maxTotal = max(total,maxTotal)
        
        return maxTotal/k
