from pomdpx_parser import pomdpx_parser as parser
import numpy as np
import xml.etree.ElementTree as ET
import copy

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

    def unpack_belief(self):
        unpacked_belief = self.belief[0]
        if len(self.belief) > 1:
            for i in range(1, len(self.belief)):
                to_calc = unpacked_belief[:]
                unpacked_belief = []
                for j in range(len(to_calc)):
                    for k in range(len(self.belief[i])):
                        unpacked_belief.append(to_calc[j]*self.belief[i][k])
        return unpacked_belief


    ## Documentation for a method.
    ## This method multiplies current belief over states with one by one policy vector.
    ## Depending on the current belief, product that gives the biggest result defines the next best action.
    ## @param self The object pointer.
    ## @returns self.optimal_actions[max_index] The number index of the best action.
    def get_optimal_action(self):
        belief = self.unpack_belief()
        max_value = 0
        max_index = 0
        index = 0
        for m in self.policy_vectors:
            if np.dot(belief, np.transpose(m)) > max_value:
                max_value = np.dot(belief, np.transpose(m))
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
        for i in range(len(self.belief)):
            T = self.transition_probs[i][action]
            O = self.observation_probs[i][action][:, self.observations[i].index(observation[i])]
            next_state_prior = np.dot(np.transpose(T), self.belief[i])
            if np.count_nonzero(next_state_prior) == 1:
                self.belief[i] = next_state_prior
            else:
                self.belief[i] = O * next_state_prior

            if np.linalg.norm(self.belief[i]) == 0:
                self.belief[i] = next_state_prior
            self.belief[i] /= np.sum(self.belief[i])

        return self.belief

    def predict_most_likely_action(self, action):
        # get most likely observation
        pomdp = copy.deepcopy(self)
        obs = [-1]*len(pomdp.belief)
        for i in range(len(pomdp.belief)):
            T = pomdp.transition_probs[i][action]
            next_state_prior = np.dot(np.transpose(T), pomdp.belief[i])
            probs = [0]*len(pomdp.observations[i])
            for j in range(len(pomdp.observations[i])):
                O = pomdp.observation_probs[i][action][:, j]
                probs[j] = np.sum(O*next_state_prior)

            obs[i] = pomdp.observations[i][probs.index(max(probs))]

        pomdp.update_belief(pomdp.actions[0][int(optA)], obs)
        return pomdp.get_optimal_action()



        # if np.count_nonzero(next_state_prior) == 1:
        #     self.belief[i] = next_state_prior
        # else:
        #     self.belief[i] = O * next_state_prior
        #
        # if np.linalg.norm(self.belief[i]) == 0:
        #     self.belief[i] = next_state_prior
        # self.belief[i] /= np.sum(self.belief[i])





if __name__ == '__main__':

    ## This is relative path to POMDPx and Policy files.
    pomdp = POMDP('../examples/HRS-planner-3.pomdpx', '../examples/HRS.policyx')

    print(len(pomdp.observations))

    obs_label = ["human", "fire"]

    print("Actions %s" % pomdp.actions[0])
    print("Observations human %s" % pomdp.observations[0])
    print("Observations fire %s" % pomdp.observations[1])
    for k in range(10):
        a = pomdp.get_optimal_action()
        print ("Optimal action %s" % pomdp.actions[0][a])
        optA = raw_input("Input action")
        print("Action taken: %s" % pomdp.actions[0][int(optA)])
        print("Most likely action in next step: %s" % pomdp.actions[0][pomdp.predict_most_likely_action(pomdp.actions[0][int(optA)])])
        obs = [-1]*len(pomdp.observations)
        for i in range(len(pomdp.observations)):
            obs_input = int(raw_input("Input %s observation" % obs_label[i]))
            obs[i] = pomdp.observations[i][obs_input]
        print("Observations: %s " % obs)
        print(pomdp.update_belief(pomdp.actions[0][int(optA)], obs))
        print(pomdp.unpack_belief())


