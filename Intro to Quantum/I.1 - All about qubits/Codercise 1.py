import numpy as np
from numpy import linalg as LA

# Here are the vector representations of |0> and |1>, for convenience
ket_0 = np.array([2.0 + 1.0j, 0])
ket_1 = np.array([0, -0.3 + 0.4j])


def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.

    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.

    Returns:
        array[complex]: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    # CREATE A VECTOR [a', b'] BASED ON alpha AND beta SUCH THAT |a'|^2 + |b'|^2 = 1
    alpha_prime = alpha / LA.norm(np.array([alpha, beta]))
    beta_prime = beta / LA.norm(np.array([alpha, beta]))

    # RETURN A VECTOR
    return np.array([alpha_prime, beta_prime])

