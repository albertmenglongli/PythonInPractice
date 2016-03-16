class Base(object):

    def __init__(self):
        pass

    def say_hello(self):
        print "hello, world!"


def say_hello_world(Class):

    def say_hello(self):
        print "hello, world! from say_hello_world"
    setattr(Class, "say_hello", say_hello)
    return Class

# in this way, we don't have to inherit the base class to just get the
# say_hello method inside


@say_hello_world
class Child(object):

    def __init__(self):
        pass

Child().say_hello()
