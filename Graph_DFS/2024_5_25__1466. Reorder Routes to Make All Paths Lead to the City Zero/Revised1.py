class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(a, parent):
            # return sum(c + dfs(b, a) for b, c in g[a] if b != parent)
            res = 0
            for nei, direction in g[a]:
                if nei != parent:         # means b is not where a comes from
                    res += dfs(nei, a) + direction
            return res
        
        g = [[] for _ in range(n)]      # Construct a graph matrix 
        for a, b in connections:
            g[a].append((b, 1))         # means the path between a and b is from a to b
            g[b].append((a, 0))         # mean the path between b and a is not from b to a 
        
        return dfs(0, -1)
                    
