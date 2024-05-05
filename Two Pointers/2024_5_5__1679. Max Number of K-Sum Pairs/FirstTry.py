class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        time,i,n= 0,0,len(nums)
        while i<n:
            j = i+1
            dreamed_num = k-nums[i]
            if nums[i] >= k:
                i += 1
                continue
            while j<n:
                if nums[j] >= k:
                    j += 1
                    continue
                if nums[j] == dreamed_num:
                    del nums[j]
                    del nums[i]
                    time += 1
                    i -= 1
                    n -= 2
                    break
                j += 1
            i += 1
        return time
