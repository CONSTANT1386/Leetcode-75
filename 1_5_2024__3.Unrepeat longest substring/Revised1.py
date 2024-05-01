# Using queue
import queue
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        q = queue.Queue()
        length = 0
        for i in range(n):
            while s[i] in list(q.queue):
                q.get()
            q.put(s[i])
            length = max(q.qsize(),length)
        return length



# Using set() as queue in python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        left = 0
        length = 0
        n = len(s)
        for i in range(n):
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
            lookup.add(s[i])
            length = max(len(lookup),length)
        return length
