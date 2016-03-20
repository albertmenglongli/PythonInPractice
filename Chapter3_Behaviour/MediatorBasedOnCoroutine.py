from collections import defaultdict


def coroutine(function):
    import functools

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


class Form(object):
    """docstring for Form"""

    def __init__(self):
        super(Form, self).__init__()
        self.create_widgets()
        self.create_mediator()

    def create_widgets(self):
        self.nameText = Text()
        self.emailText = Text()
        self.okButton = Button("OK")
        self.cancelButton = Button("Cancel")

    def create_mediator(self):
        self.mediator = self.__update_ui_mediator(self.__clicked_mediator())
        for widget in (self.nameText, self.emailText, self.okButton, self.cancelButton):
            widget.mediator = self.mediator
        self.mediator.send(None)

    @coroutine
    def __update_ui_mediator(self, successor=None):
        cnt = 0
        while True:
            cnt += 1
            widget = (yield cnt)
            if widget is not None:
                self.okButton.enabled = (
                    bool(self.nameText.text) and bool(self.emailText.text))
            if successor:
                successor.send(widget)

    @coroutine
    def __clicked_mediator(self, successor=None):
        while True:
            widget = (yield)
            if widget is not None:
                if widget == self.okButton:
                    print "OK"
                elif widget == self.cancelButton:
                    print "Cancel"
            if successor:
                successor.send(widget)


class Mediated(object):
    """docstring for Mediated"""

    def __init__(self):
        super(Mediated, self).__init__()
        self.mediator = None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.send(self)


class Button(Mediated):
    """docstring for Button"""

    def __init__(self, text=""):
        super(Button, self).__init__()
        self.enabled = True
        self.text = text

    def click(self):
        if self.enabled:
            self.on_change()


class Text(Mediated):
    """docstring for Text"""

    def __init__(self, text=""):
        super(Text, self).__init__()
        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if self.text != value:
            self.__text = Text
            self.on_change()

if __name__ == "__main__":
    form = Form()
    form.nameText.text = "menglongli"
    form.emailText.text = "albert.menglongli@gmail.com"
    form.okButton.click()
    # OK
