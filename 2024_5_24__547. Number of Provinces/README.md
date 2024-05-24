## [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75)
- ### Revised1: UnionFindSet
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
        while self.father[x] is not None: root = self.father[x]
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
