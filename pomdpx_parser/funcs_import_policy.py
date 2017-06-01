import numpy as np

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

