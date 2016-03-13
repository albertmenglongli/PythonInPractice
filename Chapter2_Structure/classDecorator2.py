def is_non_empty_str(name, value):
    if not isinstance(value, str):
        raise ValueError("{name} must be a string".format(name=name))
    if not bool(value):
        raise ValueError("{name} may not be empty".format(name=name))

class Ensure(object):
    def __init__(self, validate):
        self.validate = validate

def do_ensure(Class):
    def make_property(name, attribute):
        privateName = "__" + name
        def getter(self):
            return getattr(self, privateName)
        def setter(self, value):
            attribute.validate(name, value)
            setattr(self, privateName, value)
        setattr(Class, name, property(getter, setter))
    for name, attribute in Class.__dict__.items():
        if isinstance(attribute, Ensure):
            make_property(name, attribute)
    return Class

@do_ensure
class Book(object):
    title = Ensure(is_non_empty_str)
    def __init__(self, title):
        self.title = title

print Book("Game of the Thrown").title
print Book("12").title

