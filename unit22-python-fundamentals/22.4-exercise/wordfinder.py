from random import choice


class WordFinder:
    """Finds random words from a dictionary
    """

    def __init__(self, source):
        self.source = source
        self.all_words = (open(self.source, 'r')).readlines()

    def random(self):
        return (choice(self.all_words)).replace('\n', '')


class SpecialWordFinder(WordFinder):
    """ Returns only random words in files that have comments and blank lines
    """

    def __init__(self, source):
        super().__init__(source)

    def random(self):
        word = (super().random()).strip()

        if word[0] == '#' or word == '':
            while word[0] == '#' or word == '':
                word = (super().random()).strip()
                if (not word[0] == '#') or (not word == ''):
                    return word
        else:
            return word
