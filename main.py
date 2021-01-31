import pygame
from ball import *
from random import randint
w, h = 800, 600
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()
ball_1 = Ball(s0=[randint(100,600), randint(200, 600)], v0 = [randint(-20,20),randint(-40,40)], mass=randint(1,3), color=YELLOW)
ball_2 = Ball(s0=[randint(100,600), randint(200, 600)], v0 = [randint(-20,20),randint(-90,0)], mass=randint(1,3), color=BLUE)
ball_3 = Ball(s0=[randint(100,600), randint(200, 600)], v0 = [randint(-20,20),randint(-90,40)], mass=randint(1,3), color=GREEN)
ball_3.applyForce([-20, -40])
ball_4 = Ball(s0=[randint(100,600), randint(200, 600)], v0 = [randint(-20,20),randint(-90, 0)], mass=randint(1,3), color=WHITE)
ball_5 = Ball(s0=[randint(100,600), randint(200, 600)], v0 = [randint(-20,20),randint(-90, 0)], mass=randint(1,3), color=CYAN)
ball_6 = Ball(s0=[randint(100,600), randint(200, 600)], v0 = [randint(-20,20),randint(-90,0)], mass=randint(1,3), color=MAGENTA)

balls = [ball_1, ball_2, ball_3, ball_4, ball_5,  ball_6]

enemy = Ball(radius=30, color=RED, s0=[700, 450])

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	screen.fill(BLACK)
	for ball in balls:
		pygame.draw.circle(screen, ball.color, ball.s, ball.radius, 0)

	pygame.draw.circle(screen, enemy.color, enemy.s, enemy.radius, 0)
	pygame.display.update()
	# 적 공객체와 충돌을 감지 판단합니다
	for ball in balls:
		if ball.collide(enemy):
			enemy.color = GRAY


	# 새로운 객체들의 위치 계산
	for ball in balls:
		ball.computePos(1/60)

	# print(ball_1.s)
	clock.tick(360)

