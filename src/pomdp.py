from pomdpx_parser import *
import numpy as np
import xml.etree.ElementTree as ET

class POMDP:
    def __init__(self, model_filename, policy_filename):
        root_model = ET.parse(model_filename).getroot()
        root_policy = ET.parse(policy_filename).getroot()
        self.description, self.discount, self.states, self.actions, self.observations = get_general_info(root_model)
        self.policy_vectors, self.optimal_actions = get_policy_vectors_and_actions(root_policy)
        self.belief = get_initial_belief(root_model)
        self.transition_probs = get_transition_matrices(root_model)
        self.observation_probs = get_observation_matrices(root_model)

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
