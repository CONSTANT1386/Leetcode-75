class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        visited = set()
        
        for i in range(n):
            if i not in visited:
                queue = collections.deque([i])
                while queue:
                    j = queue.popleft()
                    visited.add(j)
                    for k in range(n):
                        if isConnected[j][k] and k not in visited:
                            queue.append(k)
                count += 1


        return count
