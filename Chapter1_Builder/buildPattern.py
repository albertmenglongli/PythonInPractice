import abc


def create_login_form(builder):
    builder.add_title("Login")
    builder.add_label("Username")
    return builder.form()


class AbstractFormBuilder(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add_title(self, title):
        self.title = title

    @abc.abstractmethod
    def add_label(self, label):
        self.label = label

    @abc.abstractmethod
    def form(self):
        pass


class HtmlFormBuilder(AbstractFormBuilder):

    def __init__(self):
        self.items = {}

    def add_title(self, title):
        super(HtmlFormBuilder, self).add_title(title)

    def add_label(self, label):
        super(HtmlFormBuilder, self).add_label(label)

    def form(self):
        html = "<!doctype html>\n<head>{title}</head>\n<body>{label}</body>\n<html>".format(
            title=self.title, label=self.label)
        print(html)

htmlForm = create_login_form(HtmlFormBuilder())
