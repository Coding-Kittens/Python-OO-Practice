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
    def __init__(self,start=0):
        self.start = start
        self.current_num = start-1

    def generate(self):
        """  Adds 1 to the current_num and returns it """
        self.current_num += 1;
        return self.current_num

    def reset(self):
        """ Sets the current_num to the start num -1
        so that when you generate the next num it equals the start num"""
        self.current_num = self.start-1
