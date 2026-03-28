import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.array(x)
    y = np.array(y)

    z = x-y
    z = np.power(z,2)
    sum = np.sum(z)

    return sum**(1/2)
    pass