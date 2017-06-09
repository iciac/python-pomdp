import numpy as np


def belief_update(current_belief, performed_action, observation_produced, state_transition_dictionary, observation_function_dictionary):

    current_belief_vector = np.transpose(current_belief)
    transition_matrix = state_transition_dictionary[performed_action]
    observation_matrix = observation_function_dictionary[performed_action]
    if observation_produced == 'yes':
        observation_vector = observation_matrix[:, 0]
    else:
        observation_vector = observation_matrix[:, 1]
    new_belief = observation_vector * np.dot(np.transpose(transition_matrix), current_belief_vector)

    return new_belief/np.linalg.norm(new_belief)
