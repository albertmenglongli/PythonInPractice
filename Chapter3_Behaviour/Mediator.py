from collections import defaultdict


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
        self.mediator = Mediator(((self.nameText, self.update_ui),
                                  (self.emailText, self.update_ui),
                                  (self.okButton, self.clicked),
                                  (self.cancelButton, self.clicked)))

    def update_ui(self, widget=None):
        self.okButton.enabled = (
            bool(self.nameText.text) and bool(self.emailText.text))
        if self.okButton.enabled:
            print"okButton is enabled"
        else:
            print"okButton is disabled"

    def clicked(self, widget):
        if widget == self.okButton:
            print "OK"
        elif widget == self.cancelButton:
            print "Cancel"


class Mediator(object):
    """docstring for Mediator"""

    def __init__(self, widgetCallablePairs):
        super(Mediator, self).__init__()
        self.callablesForWidgets = defaultdict(list)
        for widget, caller in widgetCallablePairs:
            self.callablesForWidgets[widget].append(caller)
            widget.mediator = self

    def on_change(self, widget):
        callables = self.callablesForWidgets.get(widget)
        if callables is not None:
            for caller in callables:
                caller(widget)
        else:
            raise AttributeError(
                "No on_change() method registered for {}".format(widget))


class Mediated(object):
    """docstring for Mediated"""

    def __init__(self):
        super(Mediated, self).__init__()
        self.mediator = None

    def on_change(self):
        if self.mediator is not None:
            self.mediator.on_change(self)


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
    # okButton is disabled
    form.emailText.text = "albert.menglongli@gmail.com"
    # okButton is enabled
    form.okButton.click()
    # OK
