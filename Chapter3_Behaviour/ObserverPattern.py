import itertools
import time


class Observed(object):
    """docstring for Observed"""

    def __init__(self):
        self.__observers = set()

    def observers_add(self, observer, *observers):
        for observer in itertools.chain((observer,), observers):
            self.__observers.add(observer)
            observer.update(self)

    def observer_discard(self, observer):
        self.__observers.discard(observer)

    def observers_notify(self):
        for observer in self.__observers:
            observer.update(self)


class SliderModel(Observed):
    """docstring for SliderModel"""

    def __init__(self, mininmum, value, maximum):
        super(SliderModel, self).__init__()
        # this part is needed, because if compare
        # the self.__value with current value
        self.__minimum = self.__value = self.__maximum = None
        self.mininmum = mininmum
        self.value = value
        self.maximum = maximum

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.__value != value:
            self.__value = value
            self.observers_notify()


class HistoryView(object):
    """docstring for HistoryView"""

    def __init__(self):
        super(HistoryView, self).__init__()
        self.data = []

    def update(self, model):
        self.data.append((model.value, time.time()))


class LiveView(object):
    """docstring for LiveView"""

    def __init__(self, length=40):
        super(LiveView, self).__init__()
        self.length = length

    def update(self, model):
        print "keep track of current data ", model.value

if __name__ == "__main__":
    historyView = HistoryView()
    liveView = LiveView()
    model = SliderModel(0, 0, 40)
    model.observers_add(historyView, liveView)
    for value in (7, 23, 37):
        model.value = value

    print historyView.data
