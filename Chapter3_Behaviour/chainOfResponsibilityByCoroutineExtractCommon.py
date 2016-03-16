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
def gen_handler(concrete_handle_method, successor=None):
    while True:
        report = (yield)
        concrete_handle_method(report)
        if successor:
            successor.send(report)


def check_title(report):
    print report.title


def check_content(report):
    if report.content:
        print report.content
    else:
        print "!!!Lack of content of report, with title \"{}\" ".format(report.title)


def gen_pipeline(*args):
    if not args:
        raise Exception("should at least have one handler")
    args_list = list(args)
    args_list.reverse()
    pipeline = gen_handler(args_list[0])
    for method in args_list[1:]:
        pipeline = gen_handler(method, pipeline)
    return pipeline

if __name__ == "__main__":
    # pipeline = gen_handler(check_title, gen_handler(check_content))
    check_points = [check_title, check_content]
    pipeline = gen_pipeline(*check_points)
    for r in reports:
        pipeline.send(r)
