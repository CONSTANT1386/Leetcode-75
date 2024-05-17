class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = [0] * len(spells)
        potions.sort()
        for i, x in enumerate(spells):
            res[i] = self.binarySearch(success / x, potions)
        return res

    def binarySearch(self, x: float, arr: List[int]) -> int:  
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] < x: 
                l = mid + 1
            else:
                r = mid - 1
        # at last l point to the index of the first number, who larger or equal to x
        # at last r point to the index of the last number, who smaller or equal to x
        return len(arr) - 1 - r  
      # return len(arr) - l
