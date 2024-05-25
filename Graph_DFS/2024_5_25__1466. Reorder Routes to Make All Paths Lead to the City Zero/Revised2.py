class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Initialize the adjacency list for each node
        edges = [[] for _ in range(n)]
        for a, b in connections:
            edges[a].append((b,1))        # outgoing edge from a to b (direction needs to change)
            edges[b].append((a,0))        # incoming edge from b to a (direction is correct)
            
        count = 0
        stack = [(0,-1)]
         # Perform a DFS using stack
        while stack:
            cur, parent = stack.pop()
            for nei, direction in edges[cur]:
                if nei != parent:
                    count += direction
                    stack.append((nei,cur))
        return count

                    
