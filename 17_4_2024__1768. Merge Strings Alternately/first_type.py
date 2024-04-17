class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result =''
        m = len(word1)
        n = len(word2)
        i = 0               # index of the longer word
        j = 0
        while m > 0 or n > 0:
            if m > 0:
                result += word1[i]
                i += 1
                m -= 1
            if n> 0:
                result += word2[j]
                j += 1
                n -= 1
        return result


# Note:
# More sufficiency needed in python3 !!
# 1. for string appendence, using "+=" operator instead of ".append()"
# 2. there is not shortcoming and operand such as "&&", “||” in python, instead "and", "or"
# 3. for running in vscode, using the code as followed:
# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.mergeAlternately("ab", "pqrs"))
