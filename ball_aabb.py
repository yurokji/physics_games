import pygame
from ball import *
from aabb import *
import math

w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

square_1 = AABB(mass=2, 	s0=[100, 500], v0=[20, -45], size=(20, 20),	color=GREEN)
ball_1 = Ball(s0=[200,500], v0=[35, -75], mass=1, color=BLUE)
enemy = AABB(mass=10, s0=[700, 450], size=(40, 40), color=RED)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	screen.fill(BLACK)
	
	pygame.draw.circle(screen, ball_1.color, ball_1.s, ball_1.radius, 0)
	pygame.draw.rect(screen, square_1.color, square_1.getRect(), 0)
	pygame.draw.rect(screen, enemy.color, enemy.getRect(), 0)
	# 적과 충돌 감지
	if ball_1.collide(enemy) or square_1.collide(enemy):
		enemy.color = GRAY
	else:
		enemy.color = RED
  
  
	
 # deltat만큼씩 시간을 흐른 후 현 위치를 갱신한다
	ball_1.computePos(1/60)
	square_1.computePos(1/60)
	pygame.display.update()	
	clock.tick(360)

