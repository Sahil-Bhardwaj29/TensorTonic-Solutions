import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    vv = np.asarray(v, dtype=float)
    single = vv.ndim == 1
    if single:
        vv = vv[np.newaxis, :]  # (1, 3)

    norms = np.linalg.norm(vv, axis=1, keepdims=True)  # (N, 1)
    safe_norms = np.where(norms == 0, 1, norms)         # avoid division by zero
    result = np.where(norms == 0, 0.0, vv / safe_norms) # zero-vec → zero-vec

    return result[0] if single else result
    
    pass