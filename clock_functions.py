import math

# Constants for calculations.
MAJOR_AXIS = 149.6
ECCENTRICITY = 0.017

def create_orbit_points(days, break_index):
	points = []
	for i in range(1, days + 1):
		degrees = (i * 360) / days
		radians = degrees * (math.pi / 180)
		distance = MAJOR_AXIS * ((1 - (ECCENTRICITY ** 2)) / 1 + (ECCENTRICITY * math.cos(radians)))
		points.append(distance)
	
	# Aligning minimum to day 4.
	points = points[break_index:] + points[:break_index]
	return points

def get_position(point, length, angle):
	angle = angle * (math.pi / 180)
	x = point[0] + length * math.cos(angle)
	y = point[1] + length * math.sin(angle)
	return (x, y)

