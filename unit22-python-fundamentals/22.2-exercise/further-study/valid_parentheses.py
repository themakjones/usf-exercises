def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    open_count = 0
    close_count = 0

    for char in parens:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        
        if open_count - close_count < 0:
            return False
    
    return open_count - close_count == 0

print(valid_parentheses("()"))
print(valid_parentheses("()()"))
print(valid_parentheses("(()())"))
print(valid_parentheses(")()"))
print(valid_parentheses("())"))
print(valid_parentheses("((())"))
print(valid_parentheses(")()("))