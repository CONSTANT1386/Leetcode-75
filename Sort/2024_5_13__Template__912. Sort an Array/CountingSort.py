class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        counts = Counter(nums)
        min_val = min(nums)
        max_val = max(nums)
        for x in range(min_val,max_val+1):
            if counts[x]:
                res.extend([x]*counts[x])
        return res
            
