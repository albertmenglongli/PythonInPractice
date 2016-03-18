from __future__ import print_function

# using generator to implement iterator


def AtoZ():
    idx = 0
    while True:
        if idx <= 25:
            yield chr(idx + ord("A"))
            idx += 1
        else:
            # here use break is OK, using yield IndexError doesn't work
            break

for letter in AtoZ():
    print(letter, end="")
print()

for letter in iter(AtoZ()):
    print(letter, end="")
print()

# using class to implement interator


class AtoZClass(object):
    """docstring for AtoZClass"""

    def __init__(self):
        super(AtoZClass, self).__init__()

    def __getitem__(self, index):
        if 0 <= index <= 25:
            return chr(index + ord("A"))
        # raise StopIteration() IndexError() are both OK
        # raise IndexError()
        raise StopIteration()

for letter in AtoZClass():
    print(letter, end="")
print()

for letter in iter(AtoZClass()):
    print(letter, end="")
print()


class President(object):
    """to be used by iter with two paramter, class must implement __call__ method"""
    __names = ("George Washington", "John Adams", "Thomas Jefferson",
               "Bill Clinto", "George W. Bush", "Barack Obama")

    def __init__(self, first=None):
        super(President, self).__init__()
        self.index = (-1 if first is None else President.__names.index(first) - 1)

    def __call__(self):
        self.index += 1
        if self.index < len(President.__names):
            return President.__names[self.index]
        # IndexError doesn't work here, must use StopIteration
        raise StopIteration()

for president in iter(President(), None):
    print(president, end=", ")
print()

