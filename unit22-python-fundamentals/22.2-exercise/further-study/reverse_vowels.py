def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    order_vowels = []
    idx_to_change = []
    curr = 0
    str_lst = list(s)
    
    for ltr in str_lst:
        if ltr in 'aeiouAEIOU':
            order_vowels.append(ltr)
            idx_to_change.append(str_lst.index(ltr,curr))
        curr += 1
    rev_vowels = order_vowels.copy()
    rev_vowels.reverse()

    for idx in idx_to_change:
         str_lst[idx] = rev_vowels[idx_to_change.index(idx)]
    
    return ''.join(str_lst)

print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))