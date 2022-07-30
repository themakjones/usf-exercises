def print_upper_words(words, letters):
    """ Prints each word from a list in uppercase
        Ex: print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
        Prints : "HELLO" "HEY" etc.
    """

    for word in words:
        if word[0] == letters:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], "h")