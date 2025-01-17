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

    return z_rotation @ xy_components
    

print(get_corrections(3,5))
