import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def many_rotations():
    """Implement the circuit depicted above and return the quantum state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT
    qml.Hadamard(wires=0)
    qml.S(wires=0)
    qml.adjoint(qml.T)(wires=0)
    qml.RZ(0.3, wires=0)
    qml.adjoint(qml.S)(wires=0)

    # RETURN THE STATE

    return qml.state()

@qml.qnode(dev)
def many_rotations2():
    """Implement the circuit depicted above and return the quantum state.

    Returns:
        array[complex]: The state of the qubit after the operations.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # IMPLEMENT THE CIRCUIT
    qml.Hadamard(wires=0)
    qml.RZ((np.pi)/2, wires=0)
    qml.adjoint(qml.RZ)(np.pi/4, wires=0)
    qml.RZ(0.3, wires=0)
    qml.adjoint(qml.RZ)(np.pi/2, wires=0)

    # RETURN THE STATE

    return qml.state()
