import lxml.etree as ET

dom = ET.parse('catalog.xml')
xslt = ET.parse('template.xsl')
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))

outfile = open("catalog.html", 'a')
outfile.write(str(ET.tostring(newdom, pretty_print=True)))