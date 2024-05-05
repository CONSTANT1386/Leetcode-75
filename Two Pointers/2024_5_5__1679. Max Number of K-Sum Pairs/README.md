## [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/description/)
- ### FirstTry: Violent Enumeration, still Overtime!
    - #### Enumerate from both sides, Time Complexity: $O(n^{2})$
    - #### skip the current element if `nums[i]` or `nums[j]` > `k` 
