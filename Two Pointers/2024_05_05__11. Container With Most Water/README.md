## [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75)
- ### FirstTry: Violent Enumerate -- Overtime！
    - #### How to reduce the time consume?
    - #### In my first try, I try to calculate the volume from the largest width, i.e. `height[0]` and `height[-1]`, That's right
    - #### When it comes to reduce the time, you can make a judge first: when the `left` and `right` pointer converge to another edge, if the height `height[right]` is smaller than `height[right+1]`, are there any need to calculate the area and minimun again?
- ### Revised1: Double pointer
    - #### Time Complexity: $O(n^{2}) -> O(n)$
        - #### Consider the both pointers at one time
        - #### For every time in loop, converge the smaller pointer, the other one is unnecessary
    - #### Reduce the unneceesary calculation for `min` and `area` in each time
        - #### Each time, if `height[right]` smaller than `height[right+1]` or `height[left]` smaller than `height[left-1]`, dont need to calculate the area and minimum
     
- ## Conclusion: How to reduce time consume
    - ### Reduce time complexity from $O(n^{2})$ to $O(n)$: Consider both pointer at one time
    - ### Reduce unnecessary calculation: Some obvious calculation can be reduced in intuition of math
