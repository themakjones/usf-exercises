def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

    rep_phrase = []
    if not type(num) == int:
        return None
    else:
        if num > 0:
            for x in range(1, num):
                rep_phrase.append(phrase)
            return ''.join(rep_phrase)
        elif num == 0:
            return ''
        else:
            return None

print(repeat('*', 3))
print(repeat('abc', 2))
print(repeat('abc', 0))
print(repeat('abc', -1))
print(repeat('abc', 'nope'))