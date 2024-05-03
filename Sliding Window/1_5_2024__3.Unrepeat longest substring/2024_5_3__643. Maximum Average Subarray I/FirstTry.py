class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def sum(nums:List):
            sum = 0
            for num in nums:
                sum += num
            return sum

        left = len(nums) - k
        q = nums[:k]
        large_res = sum(q)
        s = sum(q)
        while left != 0:
            q.append(nums[len(nums) - left])
            s = s+q[-1]-q[0]
            large_res = max(large_res, s)
            del q[0]
            left -= 1
            
        return large_res/k
        
        
        

            
            
