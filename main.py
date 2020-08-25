"""Write a function called replace_at_index(), which takes three parameters:

    lst - a list
    idx - an index value
    obj - an object

The function will replace the element in lst at idx with obj. You can assume that all inputs will be valid (no index will be beyond the length of a list, etc.).

Note: Be sure to follow the best practices taught in the previous lesson by not modifying the list that is passed as a parameter, but rather, a copy of that list.
"""

def replace_at_index(lst, idx, obj):
  modified_list = lst.copy()
  modified_list[idx] = obj
  return modified_list