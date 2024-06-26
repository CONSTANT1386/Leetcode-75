## [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75)
- ### Revised1: UnionFindSet -- Time Complexity $O(n^{2}logn) \approx O(n^{2})$
  - #### Traverse the representative matrix: only need to traverse the down-left triangle
  - #### Using UnionFindSet, whose module is as followed
  - #### [Explanation--UnionFindSet](https://leetcode.cn/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75)
```python
class UnionFind:
    def __init__(self):
        self.father = {}

    def add(self, x):
        if x not in self.father:
            self.father[x] = None

    def find(self, x):
        root = x
        while self.father[root] is not None: root = self.father[x]
        # when trying to find an ancestor, optimatize the depth of graph into 2
        # Optimize the speed for find next time, and merge
        while x != root:
            original_root = self.father[x]
            self.father[x] = root
            x = original_root
        return root
    
    def isConnected(self,x,y):
       px, py = self.find(x), self.find(y)      # px means parent of x, or root_x
       if px == py: return True
       return False 

    def merge(self,x,y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.father[x] = py
  ```

- ### Revised2: DFS
  - #### Use `dfs()` to execute every city in the intial matrix. For each city recursion, the first level can be seen as the parent, i.e for each parent and its all children is a province.
  - #### If the current city haven't been visited in the recursion from front cities, it will be input as a parameter of new recursion, and the add `count`
 
- ### Revised3: BFS
  - #### For each unvisited city, making a BFS, marking unvisited cities connected separately
  - #### For each BFS at the first level(i.e. the parent), it is a province
 
- ### The core of BFS and DFS is to mark the unvisited cities from a city, then to construct a whole province, the numbers of roots is exactly the number of provinces. Every time we invoke a DFS(for the first level) or BFS, that is we are constructing *one* province.
