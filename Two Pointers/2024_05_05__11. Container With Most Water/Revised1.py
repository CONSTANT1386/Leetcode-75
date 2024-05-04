class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        res = (right-left)*min(height[left], height[right])

        while(left<right):
            if height[left]<= height[right]:
                left += 1
                if height[left]<height[left-1]:
                    continue
            else:
                right -= 1
                if height[right] < height[right+1]:
                    continue
            area = (right-left)*min(height[left], height[right])
            res = max(area, res)    

        return res
