import math
import numpy as np

def get_corrections(error_angle_deg: float, error_magnitude: float) -> np.ndarray:
    """
    Computes the components of the correction in XY plane

    Parameters:
    error_angle_deg (float): The error angle in degrees.
    error_magnitude (float): The magnitude of the error vector in mms.

    Returns:
    np.ndarray: A 2x1 numpy array representing the corrected vector components in the XY-plane after applying the rotation.

    Raises:
    ValueError: If the determinant of the rotation matrix is not 1 or -1, indicating an invalid rotation matrix.
    """    
    error_angle_rads = math.radians(error_angle_deg)
    xy_components = np.array(
        [
            [error_magnitude * math.cos(error_angle_rads)],
            [error_magnitude * math.sin(error_angle_rads)],
        ]
    )

    z_rotation = np.array([
        [math.cos(error_angle_rads), math.sin(error_angle_rads)],
        [-math.sin(error_angle_rads), math.cos(error_angle_rads)],
    ])

    if np.linalg.det(z_rotation) == 1 or np.linalg.det(z_rotation) == -1: 
        return z_rotation @ xy_components
    raise ValueError("Incorrect angle leading to a determinant that's not 1 or -1")

print(get_corrections(3,5))