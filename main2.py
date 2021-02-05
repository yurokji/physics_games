import pygame
from ball import *
from poly import *
import math
from random import randint 

w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()



pts=[(50,200), (30, 220), (330, 520), (350, 500)]
ball = Ball(s0=[64,201], v0=[10, 0], mass=2, color=GREEN)
floor_1 = Polygon(mass=10, points=pts, size=(300, 10), color=WHITE)

balls = [ball]

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				balls.append(Ball(s0=[randint(20, 260),91], v0=[randint(5, 40), 0], mass=1, color=GREEN))
	
	screen.fill(BLACK)
	
	pygame.draw.circle(screen, ball.color, ball.s, ball.radius, 0)
	pygame.draw.polygon(screen, floor_1.color, pts, 0)


	collided_1 = ball.collide(floor_1)
	if collided_1:
		floor_1.color = GRAY
	else:
		floor_1.color = RED
	ball.computePos(collided_1, False, 1/60)

			
	pygame.display.update()	
	clock.tick(360)

