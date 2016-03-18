class Bag(object):
    """docstring for Bag"""

    def __init__(self, items=None):
        super(Bag, self).__init__()
        self.__bag = {}
        if items is not None:
            for item in items:
                self.add(item)

    def add(self, item):
        self.__bag[item] = self.__bag.get(item, 0) + 1

    def delitem(self, item):
        if self.__bag.get(item) is not None:
            self.__bag[item] -= 1
            if self.__bag[item] <= 0:
                del self.__bag[item]
        else:
            raise KeyError()

    def count(self, item):
        return self.__bag.get(item, 0)

    def __len__(self):
        return sum(value for value in self.__bag.values())

    def __contains__(self, item):
        return item in self.__bag.keys()

    def __iter__(self):
        for item, value in self.__bag.items():
            for _ in range(value):
                yield item
        # return (item for item, value in self.__bag.items() for _ in
        # range(value))

bag = Bag()

bag.add("orange")
for i in range(5):
    bag.add("apple")

print bag.count("apple")
print len(bag)

print "apple" in bag

for item in bag:
    print item
print end - start
