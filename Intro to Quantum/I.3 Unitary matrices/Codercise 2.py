import pennylane as qml
dev = qml.device("default.qubit", wires=1)

"""
This function parameterizes the Unitary function by giving in the precise angles
"""
@qml.qnode(dev)
def apply_u_as_rot(phi, theta, omega):
    ##################
    # YOUR CODE HERE #
    ##################

    # APPLY A ROT GATE USING THE PROVIDED INPUT PARAMETERS
    qml.Rot(phi, theta, omega, wires=0)

    # RETURN THE QUANTUM STATE VECTOR
    return qml.state()
