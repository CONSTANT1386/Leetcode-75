class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for left in range(n):
            for right in range(n-1,-1,-1):
                area = (right - left)*min(height[left], height[right])
                res = max(res, area)
        return res
