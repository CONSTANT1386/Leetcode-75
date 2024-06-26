class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed = [0] + flowerbed  
        N = len(flowerbed)
        i = 1
        while i < N:
            if sum(flowerbed[i-1:i+2]) == 0:
                n -= 1
                i += 1
            if n <= 0:
                return True
            i += 1
    
        return False


# IDEA: check every 3 item as a group
# IDEA: for a new plant, check for the next item is not necessary, thereby gap 2 index, moreover, it hasn't edit the input list itself
# optimization: return immediately as the n reach zero, reduce the following calculation

#Python: in python if the end index of slice is surpass the length of list, that's okey!
