import xml.etree.ElementTree as ET
e=ET.parse('../examples/Tiger.pomdpx').getroot()
tree = ET.parse('../examples/Tiger.pomdpx')
root = tree.getroot()
for child in root:
    print child.tag, child

