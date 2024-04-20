class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        front_zero = True 
        next_zero = False
        count = 0
        for index, plot in enumerate(flowerbed):
            if plot:
                front_zero = False
                continue
            if index == len(flowerbed) - 1:
                next_zero = True
            elif flowerbed[index+1] == 0:
                next_zero = True
            else:
                next_zero = False
            if front_zero and next_zero:
                plot = 1
                count += 1
                front_zero = False
            else:
                front_zero = True
            
        return count >= n

# Not rapid! Not clear!!
