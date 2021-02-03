import pygame
from ball import *
from aabb import *
import math

w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

square1 = AABB(mass=2, 	s0=[100, 500], v0=[40, -75], size=(20, 20),	color=GREEN)
enemy = AABB(mass=10, s0=[700, 450], size=(40, 40), color=RED)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	screen.fill(BLACK)
	pygame.draw.rect(screen, square1.color, square1.getRect(), 0)
	pygame.draw.rect(screen, enemy.color, enemy.getRect(), 0)
	# 적과 충돌 감지
	if square1.collide(enemy):
		enemy.color = GRAY
	else:
		enemy.color = RED
	# deltat만큼씩 시간을 흐른 후 현 위치를 갱신한다
	square1.computePos(1/60)
	pygame.display.update()	
	clock.tick(360)

