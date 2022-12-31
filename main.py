import pygame
import clock_functions as cf
from random import randint

months_to_days = {"Jan":31, "Feb":28, "Mar":31, "Apr":30,
					"May":31, "Jun":30, "Jul":31, "Aug":31,
					"Sep":30, "Oct":31, "Nov":30, "Dec":31}

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
				months_to_days["Feb"] = 29
			else:
				days, break_index = 365, 178
				months_to_days["Feb"] = 28
			points = cf.create_orbit_points(days, break_index)
			trail = [0 for i in range(0, days)]

		# Show the background.
		screen.blit(bg, (0, 0))

		# Drawing the clock face.
		face_angle = 270
		for key in months_to_days.keys():
			posA = cf.get_position(CENTER, 170, face_angle)
			posB = cf.get_position(CENTER, 200, face_angle)
			pygame.draw.aaline(screen, (255,255,255), posA, posB, 2)
			face_angle += (360 / days) * months_to_days[key]

		# Drawing trail effect for earth.
		trail[count] = 100
		for index, value in enumerate(trail):
			if value > 20:
				angle = 270 + (index / days) * 360
				position = cf.get_position(CENTER, points[index]/1.5, angle)
				pygame.draw.circle(screen, (value,value,value), position, 1)
				trail[index] -= 1

		# Drawing the Earth and the clock hand.
		angle = 270 + (count / days) * 360
		position_hand = cf.get_position(CENTER, 145, angle)
		pygame.draw.aaline(screen, (255,255,255), CENTER, position_hand)
		position_earth = cf.get_position(CENTER, points[count]/1.5, angle)
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
