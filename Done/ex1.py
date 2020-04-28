import xml.sax


class PersonneHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentTag = ""
        self.charBuffer = []
        self.paddingCounter = 0

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentTag = tag
        if tag == "email":
            email = attributes["adresse"]
            print(f"{email}")

    # Call when an elements ends
    def endElement(self, tag):
        pass

    # Call when a character is read
    def characters(self, content):
        self.charBuffer.append(content)


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = PersonneHandler()
    parser.setContentHandler(Handler)

    parser.parse("carnet.xml")
