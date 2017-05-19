import xml.etree.ElementTree as ET
import numpy as np

root = ET.parse('../examples/functional_imitation.policy').getroot()

def importPolicy():

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

