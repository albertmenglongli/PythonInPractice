from chainOfResponsibility import Report, reports
import functools


def coroutine(function):
    """
    this decorator will run the first next of the generator
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def title_handler(successor=None):
    while True:
        report = (yield)
        print report.title
        if successor:
            successor.send(report)


@coroutine
def content_handler(successor=None):
    while True:
        report = (yield)
        if report.content:
            print report.content
        else:
            print "!!! Lack of content of {}".format(report.title)
        if successor:
            successor.send(report)

if __name__ == "__main__":
    pipeline = title_handler(content_handler())
    for r in reports:
        pipeline.send(r)
