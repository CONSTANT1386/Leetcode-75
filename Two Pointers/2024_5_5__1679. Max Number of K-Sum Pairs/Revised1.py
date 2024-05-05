class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        res = 0
        n = len(nums)
        for num in nums:
            if num>=k:
                continue
            if cnt[k-num]:
                cnt[k-num] -= 1
                res += 1
            else:
                cnt[num] += 1
        return res
