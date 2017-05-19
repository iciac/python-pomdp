import numpy as np


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
