import pygame
from ball import *
from poly import *
import math
from random import randint 



	
w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

pts=[(-50,100), (-70, 120), (330, 520), (350, 500)]

# balls = [ball]
r = 100
running = True
rotation_angle = math.radians(-90)
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:

			running = False
		# elif event.type == pygame.KEYDOWN:
			# if event.key == pygame.K_SPACE:
			# 	balls.append(Ball(s0=[randint(20, 260),91], v0=[randint(5, 40), 0], mass=1, color=GREEN))
	
	screen.fill(BLACK)
	

	# pygame.draw.circle(screen, ball.color, ball.s, ball.radius, 0)
	
	# pts=[[50,200], [30, 220], [330, 520], [350, 500]]
	pts=[[100,100], [150, 200], [200, 200], [200, 150]]
	
	for i, pt in enumerate(pts):
		x = pt[0] - w//2
		y = pt[1] - h//2
		x = (x * math.cos(rotation_angle) - y * math.sin(rotation_angle)) + w//2
		y = (x * math.sin(rotation_angle) + y * math.cos(rotation_angle)) + h//2
	
		pts[i] = [x, y]
	

	
	print(pts)
	# input()
	# # ball = Ball(s0=[50,173], v0=[0, 0], radius=20, mass=2, color=GREEN)
	# floor_1 = Polygon(mass=10, points=pts, size=(300, 10), color=WHITE)
	pygame.draw.polygon(screen, WHITE, pts, 0)


	# collided_1 = ball.collide(floor_1)
	# if collided_1:
	# 	floor_1.color = GRAY
	# else:
	# 	floor_1.color = RED
	# ball.computePos(collided_1, False, 1/60)

			
	pygame.display.update()	
	clock.tick(360)
	# rotation_angle += 0.001
	# if rotation_angle >= 6.13:
	# 	rotation_angle = 0

