# Gain
- To traverse a list, **which used as a stack**, you should notice there is the <mark>change of list length, **while traverse is on**</mark>

```python
  # This is not suitable
  for word in range(len(list)):
    result += ''.join(list.pop())
    if word != len(list) -1:          #The len(list) is changing aboved
      result += ' '

  # This is right
  n = len(list)
  for word in range(n):
    result += ''.join(list.pop())
    if word != n-1:
      result += ' '
```

