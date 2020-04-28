import xml.etree.ElementTree as ET

racine = ET.Element("carnet")

# Clapton
personne = ET.SubElement(racine, "personne", nom="Clapton", numero="A0000")

contact = ET.SubElement(personne, "contact-info")
comment = ET.Comment("Confidential")
contact.insert(0, comment)

ET.SubElement(personne, "adresse", ville="Los Angeles", rue="Pine Rd.", numero="1239", pays="CA")
ET.SubElement(personne, "job-info", iscadre="no", jobdescription="cadre", typedemploi="temps-plein")

# Hendrix
personne = ET.SubElement(racine, "personne", nom="Hendrix", prenom="jimi", numero="A7000")
contact = ET.SubElement(personne, "contact-info")
ET.SubElement(contact, "email", adresse="jimi.hendrix@audiens.fr")
ET.SubElement(contact, "telephonedomicile", numero="0202020202")
ET.SubElement(personne, "adresse", ville="New York", rue="118 St.", numero="344", pays="NY")
ET.SubElement(personne, "job-info", iscadre="no", jobdescription="Group Leader", typedemploi="temps-plein")

tree = ET.ElementTree(racine)
tree.write("carnet.xml")
