class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        m = max(candies)
        for kid in candies:
            if kid + extraCandies >= m:
                result.append(True)
            else:
                result.append(False)
        return result

