## [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75)
- ### FirstTry: DFS
  - #### It's really important to pay attention to the condition of `enter the recursion method`, which means how can a recursion end.
  - #### Pass a list as parameter to keep record in the recursion
``` python
def dfs(keys:List[int], r:List[int]):
            if keys:
                for key in keys:
                    if r[key] == 0:
                        r[key] = 1          # this line should be before the next line, because this related to whether a recursion method could happen for the next generations
                        dfs(rooms[key],r)
```
- ### Revised1: BFS
  - #### Notice what we append in `queue`, is it a `List[int]` or `int`?
