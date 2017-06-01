'''
import numpy as np
a=np.arange(4)
b=np.transpose(a)
print a
print b
c=np.dot(a,a)
print c

Nesto = np.arange(9).reshape(3,3)
Stupac = Nesto[:,0]
print Nesto
print Stupac

umnozak1=np.dot(Stupac, Stupac)
umnozak2=np.dot(Stupac, np.transpose(Stupac))

print umnozak1, umnozak2
'''
'''
StateTransitionDictionary={}
for k in root.findall('StateTransitionFunction'):
    for m in k.findall('CondProb'):
       for n in m.findall('Parameter'):
            for o in n.findall('Entry'):
                key = o.find('Instance').text.split(' ')[0]
                for p in o.findall('ProbTable'):
                    StateTransitionList=[]
                    pom2=p.text.split('\n')
                    for x in pom2:
                        pom3=x.split(' ')
                        for y in pom3:
                            if y!='':
                                StateTransitionList.append(float(y))
                StateTransitionVector=np.array(StateTransitionList).reshape(7,7)
                StateTransitionDictionary[key] = StateTransitionVector
print(StateTransitionDictionary['end'])


ObservationFunctionDictionary={}
for k in root.findall('ObsFunction'):
    for m in k.findall('CondProb'):
       for n in m.findall('Parameter'):
            for o in n.findall('Entry'):
                key = o.find('Instance').text.split(' ')[0]
                for p in o.findall('ProbTable'):
                    ObservationFunctionList=[]
                    pom2=p.text.split('\n')
                    for x in pom2:
                        pom3=x.split(' ')
                        for y in pom3:
                            if y!='':
                                ObservationFunctionList.append(float(y))
                ObservationFunctionVector=np.array(ObservationFunctionList).reshape(7,2)
                ObservationFunctionDictionary[key] = ObservationFunctionVector
print(ObservationFunctionDictionary['end'])
'''

