class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums,0,len(nums)-1)
        return nums
    

    def quickSort(self,nums, l, r):
        if l>=r: return
        i = self.partition(nums,l,r)
        self.quickSort(nums,l,i-1)
        self.quickSort(nums,i+1,r)

    def partition(self,nums, l,r):
        # revise the pivot as a random num
        ra = random.randrange(l, r + 1)
        nums[l], nums[ra] = nums[ra], nums[l]

        i, j = l, r
        while i<j:
            # still choose l as pivot
            while i<j and nums[j]>=nums[l]: j -= 1
            while i<j and nums[i]<=nums[l]: i += 1
            nums[i],nums[j] = nums[j],nums[i]
        nums[i], nums[l] = nums[l], nums[j]
        return i
