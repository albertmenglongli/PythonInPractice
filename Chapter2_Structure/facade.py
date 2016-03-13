class Archive(object):
    """docstring for Archive"""
    def __init__(self, filename):
        super(Archive, self).__init__()
        self._names = None
        self._unpack = None
        self._file = None
        self.filename = filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, name):
        self.close()
        self.__filename = name
   
    def close(self):
        if self._file is not None:
            self._file.close()
        self._names = self._unpack = self._file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

with Archive("test") as f:
    print f.filename

        