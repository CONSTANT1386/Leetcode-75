class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        t_n = len(t)
        s_n = len(s)
        t_idx = 0
        hasFound = False
        for i in range(s_n):
            if t_idx == t_n and i != s_n:
                return False
            for j in range(t_idx, t_n):
                if s[i] == t[j]:
                    t_idx = j+1
                    hasFound = True
                    break
                else: hasFound = False
            if not hasFound:
                break
        return hasFound

            
