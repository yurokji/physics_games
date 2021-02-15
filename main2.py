import pygame
from ball import *
from poly import *
import math
from random import randint 
import numpy as np
from kd_tree import *

w, h = 1200, 900
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()




ball = Ball(s0=[100,50], v0=[0, 0], radius=10, mass=1.5, color=GREEN)
# pts1=[(-50,100), (-70, 120), (330, 520), (350, 500)]
# floor_1 = Polygon(mass=10, points=pts1, size=(300, 10), color=WHITE)
# pts2=[(330, 500), (330, 520), (530, 520), (530, 500)]
# floor_2 = Polygon(mass=10, points=pts2, size=(300, 10), color=WHITE)
# pts3=[(530,500), (510, 520), (700, 620), (700, 600)]
# floor_3 = Polygon(mass=10, points=pts3, size=(300, 10), color=WHITE)
# pts4=[(700, 600), (700, 620), (800, 620), (800, 600)]
# floor_4 = Polygon(mass=10, points=pts4, size=(300, 10), color=WHITE)



# y = (x- i)^2 + p
start_x = -30
end_x = 20
xs = np.linspace(start_x, end_x, (end_x-start_x+1)*10)
ys = xs * xs
ys = h - ys - 200
xs *= 20
xs += w//2 


objs = []
sz = len(xs)
block_width = 4
for i, x in enumerate(xs):
	if i < sz - 2:
		p1 = (xs[i],ys[i])
		p2 = (xs[i]-block_width, ys[i])
		p3 = (xs[i]-block_width, ys[i+1])
		p4 = (xs[i+1], ys[i+1])
		pts=[p1, p2, p3, p4]
		objs.append(Polygon(mass=10, points=pts, color=WHITE))
	# objs.append(pts)

# balls = [ball]

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
	# pygame.draw.polygon(screen, floor_1.color, pts1, 0)
	# pygame.draw.polygon(screen, floor_2.color, pts2, 0)
	# pygame.draw.polygon(screen, floor_3.color, pts3, 0)
	# pygame.draw.polygon(screen, floor_4.color, pts4, 0)
	
	for obj in objs:
		pygame.draw.polygon(screen, obj.color, obj.points, 0)
		pt = obj.points[0]
		normal = obj.normal.toList()
		nx = pt[0] + 30 * normal[0]
		ny = pt[1] + 30 * normal[1]
		tangent = obj.tangent.toList()
		tx = pt[0] + 10 * tangent[0]
		ty = pt[1] + 10 * tangent[1]
		pygame.draw.line(screen, (255,0,0), pt, (nx,ny))
		pygame.draw.circle(screen, (255,255,0), pt, 4, 0)
		# pygame.draw.line(screen, (0,0,255), pt, (tx,ty))


	collided = False
	for obj in objs:
		if ball.collide(obj):
			collided = True
			break
	ball.computePos(collided, 1/60)

	# elif ball.collide(floor_2):
	# 	ball.computePos(True, 1/60)
	# elif ball.collide(floor_3):
	# 	ball.computePos(True, 1/60)
	# elif ball.collide(floor_4):
	# 	ball.computePos(True, 1/60)
	# else:
	# 	ball.computePos(False, 1/60)
			
	# for x, y in zip(xs, ys):
	# 	pygame.draw.circle(screen, WHITE, (x,y), 2, 0)

	pygame.display.update()	
	clock.tick(240)
	# input()

