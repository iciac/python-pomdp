## Documentation for this module.
## This Python module parses POMDPx files and returns vectors and values that are used for belief update.

import numpy as np

## Documentation for a function.
## This function uses the root of a parsed XML policy file, parses it and returns two lists.
## First list contains policy vectors.
## Second list contains the best actions for each policy.
## @param root Root of XML policy file.
## @returns policy_vectors_field List of policy vectors.
## @returns best_action_list List of best actions.
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


## Documentation for a function.
## This function uses the root of a parsed XML POMDPx file, parses it and returns wanted dictionary
## depending on the input tag.
## @param tag Name of the tag that defines which part of POMDPx wants to be put in dictionary.
## @param root Root of XML POMDPx file.
## @returns dictionary Dictionary that connects wanted matrices with their transitions or observations.
def get_matrix(tag, root):
    for k in root.findall(tag):
        dict_list = []
        for m in k.findall('CondProb'):
            dictionary = {}
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
            dict_list.append(dictionary)
    return dict_list


## Documentation for a function.
## This function uses the root of a parsed XML POMDPx file, parses it and returns description od POMDPx
## and basic variables that define POMDP.
## First list contains policy vectors.
## Second list contains the best actions for each policy.
## @param root Root of XML POMDPx file.
## @returns description Description of POMDPx file purpose.
## @returns discount Discount.
## @returns states List of states.
## @returns actions List of actions.
## @returns observations List of possible observations.
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
            if k.tag == 'StateVar':
                if k[0].tag == 'ValueEnum':
                    states.append(k[0].text.split(' '))
                else:
                    states.append(["s%s" % x for x in range(1, int(k[0].text) + 1)])
            if k.tag == 'ActionVar':
                if k[0].tag == 'ValueEnum':
                    actions.append(k[0].text.split(' '))
                else:
                    actions.append(["a%s" % x for x in range(1, int(k[0].text) + 1)])
            if k.tag == 'ObsVar':
                if k[0].tag == 'ValueEnum':
                    observations.append(k[0].text.split(' '))
                else:
                    observations.append(["o%s" % x for x in range(1, int(k[0].text) + 1)])

    return description, discount, states, actions, observations

## Documentation for a function.
## This function uses the root of a parsed XML POMDPx file, parses it and returns initial belief over states.
## @param root Root of XML POMDPx file.
## @returns isb_vector Vector that contains initial belief over states
def get_initial_belief(root):

    for k in root.findall('InitialStateBelief'):
        isb_list = []
        for m in k.findall('CondProb'):
            isb = []
            for n in m.findall('Parameter'):
                for o in n.findall('Entry'):
                    for p in o.findall('ProbTable'):
                        pom1 = p.text.split(' ')
                        for x in pom1:
                            isb.append(float(x))
            isb_list.append(isb)

    return isb_list
