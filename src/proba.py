import xml.etree.ElementTree as ET
e=ET.parse('Tiger.pomdpx').getroot()
tree = ET.parse('Tiger.pomdpx')
root = tree.getroot()
for child in root:
    print child.tag, child

