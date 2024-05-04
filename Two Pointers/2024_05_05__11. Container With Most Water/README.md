## [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75)
- ### FirstTry: Violent Enumerate -- Overtime！
    - #### How to reduce the time consume?
    - #### In my first try, I try to calculate the volume from the largest width, i.e. `height[0]` and `height[-1]`, That's right
    - #### When it comes to reduce the time, you can make a judge first: when the `left` and `right` pointer converge to another edge, if the height `height[right]` is smaller than `height[right]`, are there any need to calculate the area and minimun again?
