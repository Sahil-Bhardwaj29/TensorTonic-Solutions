import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    v = np.array(v);
    w = np.array(w);

    z = v*w;
    dot=0
    for x in z:
        dot += x
    mag_v = 0;
    for x in v:
        mag_v += x**2
    mag_v = np.sqrt(mag_v)

    mag_w = 0;
    for x in w:
        mag_w += x**2
    mag_w = np.sqrt(mag_w)

    o = np.arccos(dot/(mag_v*mag_w))

    return o
    pass