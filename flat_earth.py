import pygame
from ball import *
from aabb import *
import math
from random import randint 

w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()


ball_1 = Ball(s0=[100,91], v0=[10, 0], mass=1, color=GREEN)
floor_1 = AABB(mass=10, s0=[50, 100], mu_k=0.9, size=(300, 10), color=WHITE)
floor_2 = AABB(mass=10, s0=[400, 400], mu_k=0, size=(300, 10), color=WHITE)

balls = [ball_1]

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				balls.append(Ball(s0=[randint(20, 260),91], v0=[randint(5, 40), 0], mass=1, color=GREEN))
	
	screen.fill(BLACK)
	
	
	pygame.draw.rect(screen, floor_1.color, floor_1.getRect(), 0)
	pygame.draw.rect(screen, floor_2.color, floor_2.getRect(), 0)
	for ball in balls:
		pygame.draw.circle(screen, ball.color, ball.s, ball.radius, 0)

	
	for i, ball in enumerate(balls):
		collided_1 = ball.collide(floor_1)
		# collided_2 = ball.collide(floor_2)
		if collided_1:
			floor_1.color = GRAY
		else:
			floor_1.color = RED
			
		# if collided_2:
		# 	floor_2.color = GRAY
		# else:
		# 	floor_2.color = RED
		ball.computePos(collided_1, False, 1/60)
		# if not ball.isValidPos((w,h)):
			
			
	pygame.display.update()	
	clock.tick(360)

