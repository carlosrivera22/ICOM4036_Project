import Element
import Style

class Paragraph(Element):

    text=""
    styles=[]
    openTag = "<p>"
    closeTag = "</p>"

    def __init__(self,text, id):
        super.__init__()

    def toString(self):
        return self.openTag+self.text+self.closeTag
