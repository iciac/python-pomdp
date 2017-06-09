from pomdpx_parser import pomdpx_parser as parser
import numpy as np
import xml.etree.ElementTree as ET


class POMDP:

    def __init__(self, model_filename, policy_filename):

        root_model = ET.parse(model_filename).getroot()
        root_policy = ET.parse(policy_filename).getroot()
        self.description, self.discount, self.states, self.actions, self.observations = parser. get_general_info(root_model)
        self.policy_vectors, self.optimal_actions = parser.import_policy(root_policy)
        self.belief = parser.get_initial_belief(root_model)
        self.transition_probs = parser.get_matrix('StateTransitionFunction', root_model)
        self.observation_probs = parser.get_matrix('ObsFunction', root_model)

    def update_belief(self, action, observation):

        T = self.transition_probs[action]
        O = self.observation_probs[action][:, self.observations.index(observation)]
        self.belief = O * np.dot(np.transpose(T), self.belief)
        # normalize belief
        self.belief /= np.linalg.norm(self.belief)
        return self.belief

    def get_optimal_action(self):

        max_value = 0
        max_index = 0
        index = 0
        for m in self.policy_vectors:
            if np.dot(self.belief, np.transpose(m)) > max_value:
                max_value = np.dot(self.belief, np.transpose(m))
                max_index = index
            index += 1

        return self.optimal_actions[max_index]


if __name__ == '__main__':

    pomdp = POMDP('../examples/functional_imitation.pomdpx', '../examples/functional_imitation.policy')
    '''for k in range(10):
        i = pomdp.belief
        a = pomdp.get_optimal_action()
        b =
    '''
    print(pomdp.actions)
    print(pomdp.observations)

    for k in range(10):
        print(pomdp.belief)
        a = pomdp.get_optimal_action()
        print (a)
        optA = input()
        obs = input()
        print (pomdp.update_belief(pomdp.actions[optA], pomdp.observations[obs] ))
'''
print(pomdp.description)
print(pomdp.discount)
print(pomdp.states)
print(pomdp.actions)
print(pomdp.observations)
print(pomdp.policy_vectors)
print(pomdp.optimal_actions)
print(pomdp.belief)
print(pomdp.transition_probs)
print(pomdp.observation_probs)
'''
