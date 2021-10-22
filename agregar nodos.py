import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file=parse('alumnosTIC.xml')

root = et.Element("TECNOLOGIASDELAINFORMACION")

xmlRoot = xml_file.getroot()

se = et.SubElement(root, "Redes_Inteligentes_ciberseguridad")
et.SubElement(se, "Nombre").text = "Pedro Perez"
et.SubElement(se, "Matricula").text = "18040555"

xmlRoot.append(se)

xml_file.write("alumnos2.xml",xml_declaration=True)


