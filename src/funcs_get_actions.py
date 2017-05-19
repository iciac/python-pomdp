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
