class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return n1 * base == str1 and n2 *  base == str2
        
        for i in range(min(len1, len2),0,-1):
            if valid(i):
                return str1[:i]
        
        return ''
                
# note:
# 1. idea: the judgement of gcd for string, can first check the length whether can be divised
# 2. "*" means repeat when operand is string
# 3. idea: to find the gcd(greatest) can sub from the end of smaller string, using
#     for i in range(min(len1, len2),0,-1):
#         str1[:i]
# 重点：先判断字符串长度是否满足gcd，再从后往前获取最大的公约字符串
