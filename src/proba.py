import xml.etree.ElementTree as ET
e=ET.parse('../examples/Tiger.pomdpx').getroot()
tree = ET.parse('../examples/Tiger.pomdpx')
root = tree.getroot()
for child in root:
    if child.tag == 'Description' or child.tag == 'Discount':
        print(child.tag, child.text)
    elif child.tag == "Variable":
        for state_var in child.findall('StateVar'):
            print(state_var.tag, state_var.attrib, state_var.text)
            value_enum = state_var.findall('ValueEnum')
            print(value_enum[0].text)
        # print(child.tag, child.list(child.tag))

