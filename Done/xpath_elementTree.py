from xml.etree.ElementTree import ElementTree

doc = ElementTree(file='carnet.xml')
for e in doc.findall('./personne'):
    print("{}".format(e.get('nom')))
    print(e.keys())
