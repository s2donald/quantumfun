import numpy as np
import pennylane as qml
dev = qml.device("default.qubit", wires=1)

U = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

"""
This function creates a circuit that applies the Unitary Matrix to the Qubit and returns the state
"""
@qml.qnode(dev)
def apply_u():

    ##################
    # YOUR CODE HERE #
    ##################

    # USE QubitUnitary TO APPLY U TO THE QUBIT
    qml.QubitUnitary(U, wires=0)

    # Return the state
    return qml.state()