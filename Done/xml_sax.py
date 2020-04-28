import xml.sax


class PersonneHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentTag = ""
        self.charBuffer = []
        self.paddingCounter = 0

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentTag = tag
        if tag == "personne":
            print("*****Personne*****")
            self.paddingCounter = 3
            nom = attributes["nom"]
            print("{0}{1}{2}".format("." * self.paddingCounter, "Nom:", nom))
            numero = attributes["numero"]
            print("{0}{1}{2}".format("." * self.paddingCounter, "Numero:", numero))
        if tag == "contact-info":
            self.paddingCounter = 3
            print("{0}{1}".format("." * self.paddingCounter, "contact-info"))

        if tag == "adresse":
            self.paddingCounter = 3
            print("{0}{1}".format("." * self.paddingCounter, "adresse"))
            self.paddingCounter = 6
            pays = attributes["pays"]
            print("{0}{1}{2}".format("." * self.paddingCounter, "Pays:", pays))
            numero = attributes["numero"]
            print("{0}{1}{2}".format("." * self.paddingCounter, "Numero:", numero))
            ville = attributes["ville"]
            print("{0}{1}{2}".format("." * self.paddingCounter, "Ville:", ville))

    # Call when an elements ends
    def endElement(self, tag):
        if tag == "contact-info":
            self.paddingCounter -= 3
            s = ''.join(self.charBuffer)
            self.charBuffer = []
            print("->", s, "<-")

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
