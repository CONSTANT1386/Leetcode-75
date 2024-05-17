## [Successful Pairs of Spells and Potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75)
- ### FirstTry: Time Complexity $O(n^{2})$
- ### Revised1: Binary Search after sort
- ### Revised2: `bisect_left` method
  - #### `bisect_left(a, x, lo=0, hi=len(a))` where `a` is an array(which is always a sorted one), `x` is the number input wanted to be found, the next two parameter is the bound(can not be input)
  - #### `bisect_search` return the value of the first index larger or equal input `x`
- ## Some Python knowledge
- ### Module for binary search:
  - #### `l` always point to the first number larger or equal to `x` at last
  - #### `r` always point to the last number smaller or equal to `x` at last
```python
l, r = 0, len(arr) - 1
    while l &lt;= r:
        mid = (l + r) // 2
        if arr[mid] &lt; x:
            l = mid + 1
        else:
            r = mid - 1
```
- ### to initialize a list with knowed length
  - #### notice the multiply is operated on `[0]`
```python
arr = [0] * len(spells)
```
