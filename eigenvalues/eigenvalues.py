import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    if len(matrix) == 0:
        return None
    if not isinstance(matrix, (list, tuple, np.ndarray)):
        return None
    
    try:
        A = np.array(matrix, dtype=float)
    except:
        return None
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return None
    # vals, vecs = np.linalg.eig(A)
    try:
        return np.linalg.eigvals(A)
    except:
        return None
    pass