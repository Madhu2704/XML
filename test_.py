import xml.etree.ElementTree as ET

name = 'test.xml'
tree = ET.parse(name)
root = tree.getroot()
ditresult = []

for child in root:
    for child1 in child:
        ditresult.append(child1.tag)

print(ditresult)
