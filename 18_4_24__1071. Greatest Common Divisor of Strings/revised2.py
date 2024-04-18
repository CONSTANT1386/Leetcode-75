from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
                
if __name__ == '__main__':
    solution = Solution()
    print(solution.gcdOfStrings('ABAB','ABABABAB'))


    # idea: FIRST CHECK: a string with gcd is consistent no matter the direction of concatenation
    # idea: the length of gcd string is the gcd of len(str1) and len(str2)

