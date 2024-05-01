class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        b = iter(t)
        return all(i in b for i in s)
