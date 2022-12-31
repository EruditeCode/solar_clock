import pygame
import math

MAJOR_AXIS = 149.6
ECCENTRICITY = 0.017

points = []
for i in range(1, 366):
	THETA = (i * 360) / 365
	RAD = THETA * (math.pi / 180)
	distance = MAJOR_AXIS * ((1 - (ECCENTRICITY ** 2)) / 1 + (ECCENTRICITY * math.cos(RAD)))
	points.append(distance)

# Aligning minimum to day 4.
points = points[178:] + points[:178]

def main():
	# Initialise pygame settings
	pygame.init()
	WIDTH, HEIGHT = 1000, 600
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Days vs Distance to Sun")
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 24)

	# Creating the background surfaces for the interface.
	bg = pygame.Surface((WIDTH, HEIGHT))
	bg.fill((20, 20, 20))

	count = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		screen.blit(bg, (0, 0))

		if count < 365:
			for i in range(0, count):
				position = (i*2 + 135 , (HEIGHT//2) - ((points[i])-149.6)*70)
				color = int((position[1] / 475) * 180)
				pygame.draw.circle(screen, (255,color,0), position, 3)
				if i == count - 1:
					pygame.draw.line(screen, (100,100,100), position, (position[0], 80), 2)
					pygame.draw.rect(screen, (100,100,100), pygame.Rect(position[0] - 50, 30, 100, 50), 2)

					text = font.render(f"{points[i]:.3f}", True, (255,255,255))
					textRect = text.get_rect()
					textRect.center = (position[0], 45)
					screen.blit(text, textRect)

					text = font.render(f"million km", True, (255,255,255))
					textRect = text.get_rect()
					textRect.center = (position[0], 65)
					screen.blit(text, textRect)

					pygame.draw.circle(screen, (255,255,255), position, 8)
		else:
			for i in range(0, count):
				position = (i*2 + 135 , (HEIGHT//2) - ((points[i])-149.6)*70)
				color = int((position[1] / 475) * 180)
				pygame.draw.circle(screen, (255,color,0), position, 3)

		if count < 365:
			count += 1

		pygame.display.update()
		clock.tick(30)


if __name__ == "__main__":
	main()
