import numpy as np
#import funcs_get_actions

def belief_update(CurrentBelief, PerformedAction, ObservationProduced, StateTransitionDictionary, ObservationFunctionDictionary):
    #PerformedAction mora biti u string formatu, tj. njeno ime

    #BestAction = funcs_get_actions.get_actions(CurrentBelief, Class.PolicyVectorsList, Class.BestActionsList)
    #BestActionName = Class.actions[BestAction]
    #OVO JE ZA SLUCAJ DA SE GET_ACTION() POZIVA IZ OVOGA PROGRAMA

    CurrentBeliefVector = np.transpose(CurrentBelief)
    TransitionMatrix = StateTransitionDictionary[PerformedAction]
    ObservationMatrix = ObservationFunctionDictionary[PerformedAction]

    if ObservationProduced == 'yes':
        ObservationVector = ObservationMatrix[:, 0]
    else:
        ObservationVector = ObservationMatrix[:, 1]

    NewBelief = ObservationVector * np.dot(np.transpose(TransitionMatrix), CurrentBeliefVector)

    return NewBelief
