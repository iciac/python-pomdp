import xml.etree.ElementTree as ET
import numpy as np
import funcs_matrix
import funcs_import_policy
import funcs_get_actions
import funcs_belief_update

root = ET.parse('../examples/functional_imitation.pomdpx').getroot()

PolicyVectorsList, BestActionsList = funcs_import_policy.importPolicy()
    #importing policy and best action vectors




class Class_general:
    def __init__(self,description,discount,states,actions,observations):
            self.description = description
            self.discount = discount
            self.states = states
            self.actions = actions
            self.observations = observations
            self.BestActionsList = BestActionsList
            self.PolicyVectorsList= PolicyVectorsList


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
        lista_nova=[]
        for k in child:
            for m in k:
                if m.tag == 'ValueEnum':
                    pom = m.text.split(' ')
                    if k.tag == 'StateVar':
                        states += pom
                    elif k.tag == 'ActionVar':
                        actions=pom
                    elif k.tag == 'ObsVar':
                        observations=pom

                elif m.tag == 'NumValue':
                    for t in range(1,int(m.text)+1):
                        if k.tag == 'StateVar':
                            states.append('s%s'%t)
                        elif k.tag == 'ActionVar':
                            actions.append('s%s'%t)
                        elif k.tag == 'ObsVar':
                            observations.append('s%s'%t)


        objekt = Class_general(description, discount, states, actions, observations)
        listaVar.append(objekt)

print(listaVar[0].states)
print(listaVar[0].observations)
print(listaVar[0].actions)


for k in root.findall('InitialStateBelief'):
       IsbList=[]
       for m in k.findall('CondProb'):
           for n in m.findall('Parameter'):
                for o in n.findall('Entry'):
                    for p in o.findall('ProbTable'):
                        pom1=p.text.split(' ')
                        for x in pom1:
                            IsbList.append(float(x))
                            IsbVector=np.array(IsbList)

print(IsbVector)



BestAction = funcs_get_actions.get_actions(IsbVector, PolicyVectorsList, BestActionsList)
print BestActionsList
print BestAction

StateTransitionDictionary = funcs_matrix.getMatrix('StateTransitionFunction', root)
ObservationFunctionDictionary = funcs_matrix.getMatrix('ObsFunction', root)

Bzvz= [0.0, 0.5, 0.25, 0.0, 0.0, 0.0, 0.25]

NewBelief = funcs_belief_update.belief_update(Bzvz, 'jump', 'no', StateTransitionDictionary, ObservationFunctionDictionary)

print("Bok")












































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
