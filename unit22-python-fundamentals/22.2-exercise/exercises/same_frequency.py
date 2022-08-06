def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    n1 = str(num1)
    n2 = str(num2)

    s1 = {(num, n1.count(num)) for num in n1}
    s2 = {(num, n2.count(num)) for num in n2}
    
    return s1 == s2

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
