"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.current = start

    def __repr__(self):
        return f'<SerialGenerator start={self.start}>'
    
    def generate(self):
        print(self.current)
        self.current += 1

    def reset(self):
        self.current = self.start
        

