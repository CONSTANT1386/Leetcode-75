## firstTry: Using numpy to caculate the array
- ### Can't directly copy one array to a new one like
  ```python
  # Wrong(where nums is a list)
  temp = nums
  # Correct
  temp = nums.copy()
  #or
  temp = nums[:]
  ```
