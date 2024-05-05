## [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/)
- ### FirstTry: Violent Enumeration, still Overtime!
    - #### Enumerate from both sides, Time Complexity: $O(n^{2})$
    - #### skip the current element if `nums[i]` or `nums[j]` > `k`
- ### Revised1: HashMap to record what's traversed
    - #### Record the times of one number appears in dictionary as the traversal going on
    - #### `Counter()` is a special type of dictionary, used to record and get the number of a element appears rapidly
    - #### Usage Example
``` python
from collections import Counter

# 创建一个 Counter 对象
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])

# 访问元素计数
print(counts['a'])  # 输出: 3
print(counts['b'])  # 输出: 2
print(counts['c'])  # 输出: 1

# 添加新元素计数
counts['d'] += 1

# 获取所有元素及其计数
print(counts)  # 输出: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})

```
- ### A similar example:[1. Two Sum](https://leetcode.com/problems/two-sum/)
