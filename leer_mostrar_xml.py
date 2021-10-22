from xml.etree import  ElementTree
import pprint
with open("alumnosTIC.xml", "rt") as f:
          tree = ElementTree.parse(f)
          
for mode in tree.iter():
          print(mode.tag)
          print(mode.text)
