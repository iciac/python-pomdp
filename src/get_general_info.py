def get_general_info(root):
'''
    class Class_general:
        def __init__(self,description,discount,states,actions,observations):
                self.description = description
                self.discount = discount
                self.states = states
                self.actions = actions
                self.observations = observations
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
            '''
            objekt = Class_general(description, discount, states, actions, observations)
            listaVar.append(objekt)
            '''
    return  objekt.description, objekt.discount, objekt.states, objekt.actions, objekt.observations
    return  objekt.description, objekt.discount, objekt.states, objekt.actions, objekt.observations
