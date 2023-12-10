import numpy as np
def measure_state(state, num_meas):
    """Simulate a quantum measurement process.

    Args:
        state (array[complex]): A normalized qubit state vector.
        num_meas (int): The number of measurements to take

    Returns:
        array[int]: A set of num_meas samples, 0 or 1, chosen according to the probability
        distribution defined by the input state.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # COMPUTE THE MEASUREMENT OUTCOME PROBABILITIES
    prob_vector = np.real(state * state.conj())

    # RETURN A LIST OF SAMPLE MEASUREMENT OUTCOMES
    return np.random.choice([0, 1], size=num_meas, p=prob_vector)

j = measure_state(np.array([0.87287156+0.43643578j, -0.13093073+0.17457431j]), 10)
print(j)