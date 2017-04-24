import xml.etree.ElementTree as ET
e=ET.parse('../examples/Tiger.pomdpx').getroot()
tree = ET.parse('../examples/Tiger.pomdpx')
root = tree.getroot()

class klasa1:
	 def __init__(self,description,discount,states,actions,observations):
            self.description = description
            self.discount = discount
            self.states = states
            self.actions = actions
            self.observations = observations


'''
for child in root:
    if child.tag == 'Description' or child.tag == 'Discount':
        print(child.tag, child.text)
    elif child.tag == "Variable":
        for state_var in child.findall('StateVar'):
            print(state_var.tag, state_var.attrib, state_var.text)
            value_enum = state_var.findall('ValueEnum')
            print(value_enum[0].text)
        # print(child.tag, child.list(child.tag))

for child in root:
    for c in child:
        for k in c.findall('Parameter'):
           for m in k.findall('Entry'):
               for n in m.findall('Instance'):
                   print (n.text)

for child in root:
    for l in child.findall('StateVar'):
        print l.attrib['vnamePrev']
        print l.attrib.keys()
'''
listaVar=[]

for child in root:
        if child.tag == 'Description':
            description = child.text
        elif child.tag == 'Discount':
            discount = float(child.text)
for child in root.findall('Variable'):
        states=[]
        actions=[]
        observations=[]
        for k in child.findall('StateVar'):
            states.append(k.attrib['vnameCurr'])
        for k in child.findall('ActionVar'):
            actions.append(k.attrib['vname'])
        for k in child.findall('ObsVar'):
            observations.append(k.attrib['vname'])
        objekt = klasa1(description, discount, states, actions, observations)
        listaVar.append(objekt)

print(listaVar[0].states)


print("Bok")
