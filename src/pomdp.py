from pomdpx_parser import pomdpx_parser as parser
import numpy as np
import xml.etree.ElementTree as ET

## Documentation for a class.
## This class contains every variable used for mathematical calculation that solves POMDPs.
## The POMDP class also contains two methods that are crucial in solving POMDPs.
class POMDP:

    ## The constructor.
    def __init__(self, model_filename, policy_filename):

        root_model = ET.parse(model_filename).getroot()
        root_policy = ET.parse(policy_filename).getroot()
        self.description, self.discount, self.states, self.actions, self.observations = parser.get_general_info(root_model)
        self.policy_vectors, self.optimal_actions = parser.import_policy(root_policy)
        self.belief = parser.get_initial_belief(root_model)
        self.transition_probs = parser.get_matrix('StateTransitionFunction', root_model)
        self.observation_probs = parser.get_matrix('ObsFunction', root_model)


    ## Documentation for a method.
    ## This method multiplies current belief over states with one by one policy vector.
    ## Depending on the current belief, product that gives the biggest result defines the next best action.
    ## @param self The object pointer.
    ## @returns self.optimal_actions[max_index] The number index of the best action.
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


    ## Documentation for a method.
    ## This method calculates the new belief over states with formula that is used for solving POMDPs.
    ## @param self The object pointer.
    ## @param action Made action.
    ## @param observation Observation based on action.
    ## @returns self.belief Updated belief.
    def update_belief(self, action, observation):

        T = self.transition_probs[action]
        O = self.observation_probs[action][:, self.observations.index(observation)]
        next_state_prior = np.dot(np.transpose(T), self.belief)
        if np.count_nonzero(next_state_prior) == 1:
            self.belief = next_state_prior
        else:
            self.belief = O * next_state_prior

        self.belief /= np.linalg.norm(self.belief)

        return self.belief


if __name__ == '__main__':

    ## This is relative path to POMDPx and Policy files.
    pomdp = POMDP('../examples/functional_imitation.pomdpx', '../examples/functional_imitation.policy')

    print(pomdp.actions)
    print(pomdp.observations)

    for k in range(10):
        print(pomdp.belief)
        a = pomdp.get_optimal_action()
        print (a)
        optA = input()
        obs = input()
        print (pomdp.update_belief(pomdp.actions[optA], pomdp.observations[obs] ))

