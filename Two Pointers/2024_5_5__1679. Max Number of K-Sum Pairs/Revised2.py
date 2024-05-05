class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        tmp = Counter(nums)
        ans = 0
        for num in tmp:
            if num * 2 < k:
                ans += min(tmp[num], tmp.get(k-num, 0))
            elif num * 2 == k:
                ans += tmp[num] // 2
        return ans
