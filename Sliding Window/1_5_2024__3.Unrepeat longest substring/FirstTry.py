class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        length = 0
        for i in range(n):
            tmp = []
            tmp.append(s[i])
            for j in range(i+1,n):
                if not s[j] in tmp:
                    tmp.append(s[j])
                else:
                    break
            length = max(length, len(tmp))
        return length        
