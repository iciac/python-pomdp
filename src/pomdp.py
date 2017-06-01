from pomdpx_parser import pomdpx_parser as parser
import numpy as np
import xml.etree.ElementTree as ET

import pomdpx_parser

class POMDP:
    def __init__(self, model_filename, policy_filename):
        root_model = ET.parse(model_filename).getroot()
        root_policy = ET.parse(policy_filename).getroot()
        self.description, self.discount, self.states, self.actions, self.observations = parser. get_general_info(root_model)
        self.policy_vectors, self.optimal_actions = parser.importPolicy(root_policy)
        self.belief = parser.get_initial_belief(root_model)
        self.transition_probs = parser.getMatrix('StateTransitionFunction', root_model)
        self.observation_probs = parser.getMatrix('ObsFunction', root_model)

    def update_belief(self, action, observation):
        T = self.transition_probs[action]
        O = self.observation_probs[action][:, self.observations.index(observation)]

        self.belief = O * np.dot(np.transpose(T), self.belief)

    def get_optimal_action(self):
        MaxIndex = 0
        Index = 0
        for m in self.policy_vectors:
            if np.dot(self.belief, np.transpose(m)) > MaxValue:
                MaxValue = np.dot(self.belief, np.transpose(m))
                MaxIndex = Index
            Index += 1
        return self.optimal_actions[MaxIndex]


if __name__ == '__main__':
	pomdp = POMDP('../examples/functional_imitation.pomdpx', '../examples/functional_imitation.policy')
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
