# Gain
- To traverse a list, **which used as a stack**, you should notice there is the <mark>change of list length, **while traverse is on**</mark>

'''python
  for word in range(len(list)):
    result += ''.join(list.pop())
'''
