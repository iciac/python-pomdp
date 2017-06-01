import numpy as np

def belief_update(CurrentBelief, PerformedAction, ObservationProduced, StateTransitionDictionary, ObservationFunctionDictionary):
    #PerformedAction mora biti u string formatu, tj. njeno ime

    CurrentBeliefVector = np.transpose(CurrentBelief)
    TransitionMatrix = StateTransitionDictionary[PerformedAction]
    ObservationMatrix = ObservationFunctionDictionary[PerformedAction]

    if ObservationProduced == 'yes':
        ObservationVector = ObservationMatrix[:, 0]
    else:
        ObservationVector = ObservationMatrix[:, 1]

    NewBelief = ObservationVector * np.dot(np.transpose(TransitionMatrix), CurrentBeliefVector)

    return NewBelief/np.linalg.norm(NewBelief)
