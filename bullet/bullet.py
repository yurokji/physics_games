import pygame
from ball import *
w, h = 1000, 800
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
# 간단한 물리 시뮬레이션 
ball = Ball(_color=GREEN, 
	 _mass= 2,
	_init_pos=[100, 500], _init_speed=[40,-40],
	 _accel=[5,0])

person_pos = (1000, 800)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(BLACK)
	pygame.draw.circle(screen, ball.color, ball.s, ball.size, 0)
	pygame.draw.circle(screen, WHITE, person_pos, 100, 0)
	ball.setPos(1/60)
	pygame.display.update()
	clock.tick(960)

