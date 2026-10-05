import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	out = {}
	out['magnitude'] = np.linalg.norm(gradient)
	out['direction'] = [num/out['magnitude'] if out['magnitude'] != 0 else 0 for num in gradient]
	out['descent_direction'] = [-num for num in out['direction']]
	return out