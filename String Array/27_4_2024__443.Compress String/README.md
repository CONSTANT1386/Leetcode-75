- ## FirstTry: Using another list to store result
    - ### Didn't satisfy the O(1) space complexity
- ## Revised1: Double pointer
    - ### `Read`: adding as traversal pointer, recording the left-edge of string group
    - ### `Write`: point to the write position, adding with every writing
    - ### `Left`: The left-edge of string group, updating when there is a writing, and its value is `read`+1 at that moment
    - ### I strong suggest to use double pointer when writing and reading in one array
- ## Revised: Double pointer, but strongly O(1)-restricted
    - ### The writing of digit when  `count` > 10 is not satisfied with O(1) space, as `str(count)` is not allowed
    - ### Creating a reversed method realized by double-pointer too. Write the digit by `while`, `count%10`, `count \\ 10` 
