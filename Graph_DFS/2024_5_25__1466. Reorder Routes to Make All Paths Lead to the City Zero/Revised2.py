class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = [[] for _ in range(n)]
        for a, b in connections:
            edges[a].append((b,1))
            edges[b].append((a,0))
        count = 0
        stack = [(0,-1)]
        while stack:
            cur, parent = stack.pop()
            for nei, direction in edges[cur]:
                if nei != parent:
                    count += direction
                    stack.append((nei,cur))
        return count

                    
