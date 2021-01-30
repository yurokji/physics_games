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

ball_1 = Ball(_radius=10,
	_color=GREEN,
	_mass=0.3,
	_s0=[100, 500],
	_v0=[20, -75],
	_a=[2, 0])
ball_2 = Ball(_radius=10,
	_color=BLUE,
	_mass=1,
	_s0=[100, 500],
	_v0=[20, -75],
	_a=[2, 0])
ball_3 = Ball(_radius=10,
	_color=YELLOW,
	_mass=2,
	_s0=[100, 500],
	_v0=[0, -75],
	_a=[0, 0])
ball_4 = Ball(_radius=10,
	_color=WHITE,
	_mass=3,
	_s0=[100, 500],
	_v0=[50, -65],
	_a=[2, 0])

print(f"degrees: {math.degrees(math.atan(ball_1.v0[1] / ball_1.v0[0]))}")


enemy = Ball(_radius=50,
	_color=RED,
	_mass=1,
	_s0=[700, 450],
	_v0=[0, 0],
	_a=[0, 0])



running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	screen.fill(BLACK)
	pygame.draw.circle(screen, ball_1.color, ball_1.s, ball_1.radius, 0)
	pygame.draw.circle(screen, ball_2.color, ball_2.s, ball_2.radius, 0)
	pygame.draw.circle(screen, ball_3.color, ball_3.s, ball_3.radius, 0)
	pygame.draw.circle(screen, ball_4.color, ball_4.s, ball_4.radius, 0)
	pygame.draw.circle(screen, enemy.color, enemy.s, enemy.radius, 0)
	# 충돌 감지
	if ball_1.collide(enemy):
		enemy.color = BLACK
	if ball_2.collide(enemy):
		enemy.color = BLACK
	if ball_3.collide(enemy):
		enemy.color = BLACK
	if ball_4.collide(enemy):
		enemy.color = BLACK
	# delta_t만큼씩 시간을 흐르게 한 후 변한 위치를 계산해서 가져온다
	ball_1.calcPos(1/60)
	ball_2.calcPos(1/60)
	ball_3.calcPos(1/60)
	ball_4.calcPos(1/60)
	pygame.display.update()	
	clock.tick(360)

