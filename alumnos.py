import xml.etree.cElementTree as et

root = et.Element("TECNOLOGIASDELAINFORMACION")
se = et.SubElement(root, "Redes_Inteligentes_ciberseguridad")

et.SubElement(se, "Nombre").text = "Aylin_Arrezola"
et.SubElement(se, "Matricula").text = "18040117"

se = et.SubElement(root, "Redes_Inteligentes_ciberseguridad")
et.SubElement(se, "Nombre").text = "Paula_Chairez"
et.SubElement(se, "Matricula").text = "18040021"

se = et.SubElement(root, "Redes_Inteligentes_ciberseguridad")
et.SubElement(se, "Nombre").text = "Victoria_Davila"
et.SubElement(se, "Matricula").text = "18040029"

se = et.SubElement(root, "Redes_Inteligentes_ciberseguridad")
et.SubElement(se, "Nombre").text = "Josue_Flores"
et.SubElement(se, "Matricula").text = "18040035"

se = et.SubElement(root, "Redes_Inteligentes_ciberseguridad")
et.SubElement(se, "Nombre").text = "Raul_Gonzalez"
et.SubElement(se, "Matricula").text = "11040095"

se = et.SubElement(root, "Desarollo_software")
et.SubElement(se, "Nombre").text = "Jhonatan_Eduardo"
et.SubElement(se, "Matricula").text = "18040048"

se = et.SubElement(root, "Desarollo_software")
et.SubElement(se, "Nombre").text = "David_Guevara"
et.SubElement(se, "Matricula").text = "16040086"

se = et.SubElement(root, "Desarollo_software")
et.SubElement(se, "Nombre").text = "Iliana_Herrera"
et.SubElement(se, "Matricula").text = "18040051"

se = et.SubElement(root, "Desarollo_software")
et.SubElement(se, "Nombre").text = "Dulce_Lopez"
et.SubElement(se, "Matricula").text = "18040058"

se = et.SubElement(root, "Desarollo_software")
et.SubElement(se, "Nombre").text = "Isidro_Mendez"
et.SubElement(se, "Matricula").text = "18040071"

se = et.SubElement(root, "Entornos_Digitales")
et.SubElement(se, "Nombre").text = "Luis_Nuncio"
et.SubElement(se, "Matricula").text = "18040161"

se = et.SubElement(root, "Entornos_Digitales")
et.SubElement(se, "Nombre").text = "Xochitl_Ovalle"
et.SubElement(se, "Matricula").text = "18040078"

se = et.SubElement(root, "Entornos_Digitales")
et.SubElement(se, "Nombre").text = "Alonso_Reyes"
et.SubElement(se, "Matricula").text = "18040151"

se = et.SubElement(root, "Entornos_Digitales")
et.SubElement(se, "Nombre").text = "Rosa_Rodriguez"
et.SubElement(se, "Matricula").text = "18040087"


tree = et.ElementTree(root)
tree.write("alumnosTIC.xml", xml_declaration=True)

