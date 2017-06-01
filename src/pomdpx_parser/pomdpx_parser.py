import numpy as np

def get_actions(Belief, PolicyVectorsList, BestActionsList):
    MaxValue=0
    Index=0
    for m in PolicyVectorsList:
        print Index
        if np.dot(Belief, np.transpose(m)) > MaxValue:
                MaxValue = np.dot(Belief, np.transpose(m))
                MaxIndex = Index
        Index +=1
    return BestActionsList[MaxIndex]


def importPolicy(root):
    for i in root.findall('AlphaVector'):
            PolicyVectorsField = []
            BestActionList = []
            for m in i.findall('Vector'):
                BestActionList.append(int(m.attrib['action']))
                pom=m.text.rstrip(' ').split(' ')
                PolicyList = []
                for x in pom:
                   PolicyList.append(float(x))
                   PolicyVector=np.array(PolicyList)
                PolicyVectorsField.append(PolicyVector)
    return PolicyVectorsField, BestActionList


def getMatrix(tag, root):
    Dictionary={}
    for k in root.findall(tag):
        for m in k.findall('CondProb'):
           for n in m.findall('Parameter'):
                for o in n.findall('Entry'):
                    key = o.find('Instance').text.split(' ')[0]
                    for p in o.findall('ProbTable'):
                        List=[]
                        pom2=p.text.lstrip('\n').rstrip('\n').rstrip(' ').split('\n')
                        pom2 = [x for x in pom2 if x is not '']
                        matrix_heigth = len(pom2)
                        for x in pom2:
                            pom3=x.split(' ')
                            matrix_width = 0
                            for y in pom3:
                                if y!='':
                                    matrix_width +=1
                                    List.append(float(y))
                    Vector=np.array(List).reshape(matrix_heigth,matrix_width)
                    Dictionary[key] = Vector

    return Dictionary


def get_general_info(root):
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
    return  description, discount, states, actions, observations

def get_initial_belief(root):
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

    return IsbVector
