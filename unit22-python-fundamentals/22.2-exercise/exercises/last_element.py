def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    
    if len(lst) == 0:
        return None
    else:
       return lst[len(lst) - 1] 
    # return len(lst)

print(last_element([1,2,3,5,97]))
print(last_element([]))