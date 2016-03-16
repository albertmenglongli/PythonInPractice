def is_float(name, value):
    if not isinstance(value, float):
        raise ValueError(name + "must be a float")


def is_non_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{name} must be a string".format(name=name))
    if not bool(value):
        raise ValueError("{name} may not be empty".format(name=name))


def ensure(name, validate):
    def decorator(Class):
        privateName = "__" + name

        def getter(self):
            return getattr(self, privateName)

        def setter(self, value):
            validate(name, value)
            setattr(self, privateName, value)
        setattr(Class, name, property(getter, setter))
        return Class
    return decorator


@ensure("price", is_float)
@ensure("title", is_non_empty_str)
class Book(object):

    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.number = 1
if __name__ == "__main__":
    b1 = Book("Harry Potter", 25.0)
    print b1.title
