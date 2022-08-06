def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    rev_str = list(phrase)
    rev_str.reverse()
    return str(rev_str)

print(reverse_string('awesome'))
print(reverse_string('sauce'))