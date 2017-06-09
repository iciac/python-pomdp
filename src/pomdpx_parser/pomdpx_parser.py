import numpy as np


def get_actions(Belief, PolicyVectorsList, BestActionsList):

    max_value = 0
    index = 0
    for m in PolicyVectorsList:
        print index
        if np.dot(Belief, np.transpose(m)) > max_value:
            max_value = np.dot(Belief, np.transpose(m))
            max_index = index
        index += 1

    return BestActionsList[max_index]


def import_policy(root):

    for i in root.findall('AlphaVector'):
        policy_vectors_field = []
        best_action_list = []
        for m in i.findall('Vector'):
            best_action_list.append(int(m.attrib['action']))
            pom = m.text.rstrip(' ').split(' ')
            policy_list = []
            for x in pom:
                policy_list.append(float(x))
                policy_vector = np.array(policy_list)
            policy_vectors_field.append(policy_vector)

    return policy_vectors_field, best_action_list


def get_matrix(tag, root):

    dictionary = {}
    for k in root.findall(tag):
        for m in k.findall('CondProb'):
            for n in m.findall('Parameter'):
                for o in n.findall('Entry'):
                    key = o.find('Instance').text.split(' ')[0]
                    for p in o.findall('ProbTable'):
                        list1 = []
                        pom2 = p.text.lstrip('\n').rstrip('\n').rstrip(' ').split('\n')
                        pom2 = [x for x in pom2 if x is not '']
                        matrix_height = len(pom2)
                        for x in pom2:
                            pom3 = x.split(' ')
                            matrix_width = 0
                            for y in pom3:
                                if y != '':
                                    matrix_width += 1
                                    list1.append(float(y))
                    vector = np.array(list1).reshape(matrix_height, matrix_width)
                    dictionary[key] = vector

    return dictionary


def get_general_info(root):

    for child in root:
        if child.tag == 'Description':
            description = child.text
        elif child.tag == 'Discount':
            discount = float(child.text)
    for child in root.findall('Variable'):
        states = []
        actions = []
        observations = []
        for k in child:
            for m in k:
                if m.tag == 'ValueEnum':
                    pom = m.text.split(' ')
                    if k.tag == 'StateVar':
                        states += pom
                    elif k.tag == 'ActionVar':
                        actions = pom
                    elif k.tag == 'ObsVar':
                        observations = pom

                elif m.tag == 'NumValue':
                    for t in range(1, int(m.text) + 1):
                        if k.tag == 'StateVar':
                            states.append('s%s' % t)
                        elif k.tag == 'ActionVar':
                            actions.append('s%s' % t)
                        elif k.tag == 'ObsVar':
                            observations.append('s%s' % t)

    return description, discount, states, actions, observations


def get_initial_belief(root):

    for k in root.findall('InitialStateBelief'):
        isb_list = []
        for m in k.findall('CondProb'):
            for n in m.findall('Parameter'):
                for o in n.findall('Entry'):
                    for p in o.findall('ProbTable'):
                        pom1 = p.text.split(' ')
                        for x in pom1:
                            isb_list.append(float(x))
                            isb_vector = np.array(isb_list)

    return isb_vector
