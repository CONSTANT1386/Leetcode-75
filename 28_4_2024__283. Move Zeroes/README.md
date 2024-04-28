- [283. Moves Zeros](https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75)
- [A nice solution](https://leetcode.cn/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75)
- ### Revised1: put the non-zero element directly in the list in order, than traverse again to fill the zeros
- ### Revised2: Traverse once
    - #### Ensuer the left of `writer` pointer is non-zero, and the right of `writer` is zeros
    - #### When do a problem like put a certain element at end, don't just focus on moving in order, using `exchange`, not only protecting the order, but move the element requiring moving
    - #### Everytime moving the non-zeros to the left of `writer` by exchanging, increase `writer`, then the left of `writer` is all non-zeros
  ```python
  # How to exchange two variables in python
  num[write], num[read] = num[read], num[write]
  ```
  
