import pygame
from ball import *
import math

w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

# 오브젝트 만들기
# 오브젝트 모양은 공 모양의 객체
# 물리시뮬레이션에 필요한 속성을 넣어준다
ball1 = Ball(mass=0.3, 	s0=[100, 500], v0=[20, -75], 	color=GREEN)
ball2 = Ball(mass=1, 	s0=[100, 500], v0=[20, -75], 	color=BLUE)
ball3 = Ball(mass=2, 	s0=[100, 500], v0=[0, -75], 	color=YELLOW)
ball4 = Ball(mass=3, 	s0=[100, 500], v0=[50, -65], 	color=WHITE)
F= [50, 0]
ball3.applyForce(F)
enemy = Ball(radius=50, color=RED, mass=1, s0=[700, 450], v0=[0, 0], a=[0, 0])

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	screen.fill(BLACK)
	# 원들을 그려준다
	pygame.draw.circle(screen, ball1.color, ball1.s, ball1.radius, 0)
	pygame.draw.circle(screen, ball2.color, ball2.s, ball2.radius, 0)
	pygame.draw.circle(screen, ball3.color, ball3.s, ball3.radius, 0)
	pygame.draw.circle(screen, ball4.color, ball4.s, ball4.radius, 0)
	pygame.draw.circle(screen, enemy.color, enemy.s, enemy.radius, 0)
	# 적과 충돌 감지
	if ball1.collide(enemy):
		enemy.color = GRAY
	if ball2.collide(enemy):
		enemy.color = GRAY
	if ball3.collide(enemy):
		enemy.color = GRAY
	if ball4.collide(enemy):
		enemy.color = GRAY
	# deltat만큼씩 시간을 흐른 후 현 위치를 갱신한다
	ball1.computePos(1/60)
	ball2.computePos(1/60)
	ball3.computePos(1/60)
	ball4.computePos(1/60)
	pygame.display.update()	
	clock.tick(360)

