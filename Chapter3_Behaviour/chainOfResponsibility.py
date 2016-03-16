from datetime import datetime


class Report(object):
    """docstring for Report"""

    def __init__(self, title, content=None, date_str=None):
        super(Report, self).__init__()
        self.title = title
        self.content = content
        self.date_str = date_str


class NullHandler(object):
    """docstring for NullHandler"""

    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, report):
        if self.__successor is not None:
            self.__successor.handle(report)


class TitleHandler(NullHandler):

    def handle(self, report):
        print report.title
        super(TitleHandler, self).handle(report)


class ContentHandler(NullHandler):

    def handle(self, report):
        if report.content:
            print report.content
        else:
            print "!!!!! Lack of content for report with title: {}".format(report.title)
        super(ContentHandler, self).handle(report)

reports = [Report("Python in Practice", "A book about OO design for python and etc.", str(datetime.now())),
           Report("Alpha Go wins", "Alpha Go win three times",
                  str(datetime.now())),
           Report("Python is cool", "", str(datetime.now()))]

if __name__ == "__main__":
    handler = TitleHandler(ContentHandler())
    for r in reports:
        handler.handle(r)
