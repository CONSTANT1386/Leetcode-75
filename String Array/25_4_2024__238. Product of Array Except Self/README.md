- ### firstTry: Using numpy to caculate the array
  - #### `Note`: Can't directly copy one array to a new one like
  ```python
  # Wrong(where nums is a list)
  temp = nums
  # Correct
  temp = nums.copy()
  #or
  temp = nums[:]
  ```
- ### revised1: caculate the  right-hand/ left-hand except-self-arrary seperatelu
  - #### `Note`: using `[0]*length(nums)` to init the list quickly
  - #### `Idea`: caculate the except-self-array from both sides
  - #### `Idea`: Using the answer caculated before to reduce time complexity

- ### revised2: only O(1) space complexity
  - #### `Note`: update and multiple `R` every time, instead of using additional list `R[]`
  - #### `Note`: the return list in github isn't marked as additonal list