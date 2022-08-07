def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    lst = (phrase.lower()).split(' ')

    for word in lst:
        lst[lst.index(word)] = word.capitalize()
    return ' '.join(lst)

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))