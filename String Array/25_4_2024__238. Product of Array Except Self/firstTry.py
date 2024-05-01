import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]):
        index = 0
        result = []
        for i in range(len(nums)):
            temp = nums.copy()
            del temp[i]
            arr = np.array(temp)
            result.append(np.prod(arr))
        return result
