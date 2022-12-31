import pygame
import clock_functions as cf
from random import randint

def main():
	# Pygame Setup
	pygame.init()
	WIDTH, HEIGHT = 1000, 600
	CENTER = (WIDTH//2, HEIGHT//2)
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()

	# Creating the background surface for the clock.
	bg = pygame.Surface((WIDTH, HEIGHT))
	bg.fill((20, 20, 20))

	# Initial setup for the clock.
	count = 0
	year = None
	days = None
	break_index = None
	points = []

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		# Collect info...
		date_year = 2023
		
		# Update orbit points based on collected information.
		if date_year != year or points == []:
			year = date_year
			if year % 4 == 0:
				days, break_index = 366, 179
			else:
				days, break_index = 365, 178
			points = cf.create_orbit_points(days, break_index)

		# Show the background.
		screen.blit(bg, (0, 0))

		# Drawing the Earth and the clock hand.
		angle = (count / days) * 360
		position_earth = cf.get_position(CENTER, points[count], angle)
		pygame.draw.circle(screen, (255,255,255), position_earth, 7)
		pygame.draw.circle(screen, (0,128,128), position_earth, 6)

		# Drawing the Sun.
		extra_radius = randint(11, 14)
		pygame.draw.circle(screen, (255,255,100), CENTER, extra_radius, 2)
		pygame.draw.circle(screen, (255,255,60), CENTER, 11)

		if count < days - 1:
			count += 1
		else:
			count = 0

		pygame.display.update()
		clock.tick(60)


if __name__ == "__main__":
	main()
