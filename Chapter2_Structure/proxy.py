class Calculator(object):
    """docstring for Calculator"""

    def __init__(self, init_num=None):
        super(Calculator, self).__init__()
        if init_num:
            self.result = init_num
        else:
            self.result = 0

    @property
    def result(self):
        return self._result_cached

    @result.setter
    def result(self, value):
        self._result_cached = value

    def add(self, num):
        self.result += num
        return self.result

    def minus(self, num):
        self.result -= num
        return self.result

    def clear(self):
        self.result = 0


class CalProxy(object):
    """
    docstring for CalProxy
    this proxy introduce cach, multi add/minus method, commands mode for lazy calculating
    """

    def __init__(self, CalculatorClass, init_num=None):
        super(CalProxy, self).__init__()
        self.Calculator = CalculatorClass
        self.commands = [(self.Calculator, init_num)]
        self._result_cached = None

    def add(self, *args):
        for i in args:
            self.commands.append((self.Calculator.add, i))
        self._result_cached = None

    def minus(self, *args):
        for i in args:
            self.commands.append((self.Calculator.minus, i))
        self._result_cached = False

    @property
    def result(self):
        if self._result_cached:
            return self._result_cached
        else:
            command = self.commands[0]
            (function, args) = command[0], command[1:]
            calculator = function(*args)
            for c in self.commands[1:]:
                function, args = c[0], c[1:]
                function(calculator, *args)
            self._result_cached = calculator.result
            return self._result_cached

    def clear(self):
        self.commands = [self.commands[0]]
        self._result_cached = None

myCal = CalProxy(Calculator)
myCal.add(1, 2, 3, 4)
myCal.minus(20)
print myCal.result

myCal.add(5)
print myCal.result

myCal.clear()
print myCal.result
myCal.add(1, 2)
print myCal.result
