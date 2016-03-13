def create_diagram(factory):
    rectangle = factory.make_rectangle(50,6)
    text = factory.make_text("this is testing for abstractory factory")
    diagram = factory.make_diagram(rectangle, text)
    return diagram

class TextBase(object):
    def __init__(self, content):
        self.content = content

class DiagramBase(object):
    def __init__(self, rectangle, text):
        self.rectangle = rectangle
        self.text = text

    def show_diagram(self):
        print "Not implemented yet!"

class RectangleBase(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class DiagramFactory(object):

    @classmethod
    def make_rectangle(klass, width, height):
        return klass.Rectangle(width, height)

    @classmethod
    def make_text(klass, content):
        return klass.Text(content)

    @classmethod
    def make_diagram(klass, rectangle, text):
        return klass.Diagram(rectangle, text)

class PureTextDiagramFactory(DiagramFactory):
    class Rectangle(RectangleBase):
        def __init__(self, width, height):
            super(PureTextDiagramFactory.Rectangle,self).__init__(width, height)

    class Text(TextBase):
        def __init__(self, content):
            super(PureTextDiagramFactory.Text, self).__init__(content)

    class Diagram(DiagramBase):
        def __init__(self, rectangle, text):
            super(PureTextDiagramFactory.Diagram, self).__init__(rectangle, text)

        def show_diagram(self):
            width = self.rectangle.width
            height = self.rectangle.height
            content = self.text.content
            print "+","-"*width,"+"
            for i in range(0,height/2):
                print "|"," "*width,"|"
            if width < len(content):
                content = content[0:width]
            print "|",
            print content,
            leftSpace = width - len(content)
            for i in range(leftSpace):
                print "",
            print "|"
            for i in range(0,height/2):
                print "|"," "*width,"|"
            print "+","-"*width,"+"

class HTMLDiagramFactory(DiagramFactory):
    class Rectangle(RectangleBase):
        def __init__(self,width,height):
            super(HTMLDiagramFactory.Rectangle, self).__init__(width, height)

    class Text(TextBase):
        def __init__(self, content):
            super(HTMLDiagramFactory.Text,self).__init__(content)

    class Diagram(DiagramBase):
        def __init__(self, rectangle, text):
            super(HTMLDiagramFactory.Diagram, self).__init__(rectangle,text)

        def show_diagram(self):
            results = '<div style="width={width}; height={height}">{content}</div>'\
                .format(width=self.rectangle.width,height=self.rectangle.height,content=self.text.content)
            print results

def main():
    diagram = create_diagram(PureTextDiagramFactory)
    diagram.show_diagram()
    diagram = create_diagram(HTMLDiagramFactory)
    diagram.show_diagram()

if __name__=="__main__":
    main()
