class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result =''
        m = len(word1)
        n = len(word2)
        i = 0               
        while i < max(m,n):
            if i < m:
                result += word1[i]
            if i < n:
                result += word2[i]
            i += 1
        return result

      
# Using only one pointer!
