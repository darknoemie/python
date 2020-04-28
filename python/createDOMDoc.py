'''

@author: phil

<carnet>
  <personne numéro-d-employé="A0000" nom-de-famille="Gates" prénom="Bob">
    <contact-info>
      <!--Confidential-->
    </contact-info>
    <adresse ville="Los Angeles" rue="Pine Rd." numéro="1239" pays="CA"/>
    <job-info is-cadre="no" job-description="cadre" type-d-emploi="temps-plein"/>
    <cadre numéro-d-employé="A0000"/>
  </personne>
  <personne numéro-d-employé="A7000" nom-de-famille="Brown" prénom="Robert" initiales="L.">
    <contact-info>
      <email adresse="robb@iro.ibm.com"/>
      <téléphone-domicile numéro="03-3987873"/>
    </contact-info>
    <adresse ville="New York" rue="118 St." numéro="344" pays="NY"/>
    <job-info is-cadre="yes" job-description="Group Leader" type-d-emploi="temps-plein"/>
    <cadre numéro-d-employé="A0000"/>
  </personne>
....
....
</carnet>

'''

import xml.etree.ElementTree as ET

racine = ET.Element("carnet")

# Clapton
personne = ET.SubElement(racine, "personne", nom="Clapton", numero="A0000")

contact=ET.SubElement(personne, "contact-info")
comment=ET.Comment("Confidential")
contact.insert(0,comment)

ET.SubElement(personne, "adresse",ville="Los Angeles", rue="Pine Rd.", numero="1239", pays="CA")
ET.SubElement(personne, "job-info",iscadre="no", jobdescription="cadre", typedemploi="temps-plein")

# Hendrix
personne = ET.SubElement(racine, "personne", nom="Hendrix",prenom="jimi", numero="A7000")
contact = ET.SubElement(personne, "contact-info")
ET.SubElement(contact, "email", adresse="jimi.hendrix@audiens.fr")
ET.SubElement(contact, "telephonedomicile", numero="0202020202")
ET.SubElement(personne, "adresse",ville="New York", rue="118 St.", numero="344", pays="NY")
ET.SubElement(personne, "job-info",iscadre="no", jobdescription="Group Leader", typedemploi="temps-plein")

tree = ET.ElementTree(racine)
tree.write("carnet.xml")