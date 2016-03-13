class Point(object):
    """docstring for Point"""
    __slots__ = ("x", "y", "z", "color")
    def __init__(self, x=0, y=0, z=0, color=None):
        super(Point, self).__init__()
        self.x =x 
        self.y =y 
        self.z =z 
        self.color =color 
        