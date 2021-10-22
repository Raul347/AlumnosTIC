from xml.etree.ElementTree import parse, Element

file_name = "alumnos2.xml"
doc_xml = parse(file_name)
root = doc_xml.getroot()

root.remove(root.find("Redes_Inteligentes_ciberseguridad"))

new_file = "alumnos3.xml"
doc_xml.write(new_file, xml_declaration=True)

