import numpy as np

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
