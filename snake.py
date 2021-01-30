from pygame import Rect, QUIT, KEYDOWN, K_w, K_s, K_a, K_d
import pygame as pg
from random import randint

def collide(head, prey):
	if abs(head.center[0] - prey.center[0]) < body_size:
		if abs(head.center[1] - prey.center[1]) < body_size:
			return True
	return False


WHITE = (255, 255, 255)
BLACK = (0 ,0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
CYAN = (255, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
pg.init()
clock = pg.time.Clock()
w, h = 800, 600
body_size = 10
gap = 0
num_body = 3
snake_body = []
for i in range(num_body):
	snake_rect = Rect(w//2 + i *body_size + i*gap, h//2, body_size, body_size)
	snake_body.append(snake_rect)
screen = pg.display.set_mode((w,h))
running = True
rot_type = 'l'
rot_end = True

start_t = 0
end_t = 0
prey = Rect(randint(body_size *2 , w -body_size * 2), 
	randint(body_size *2, h - body_size*2), body_size, body_size)
something = True
j = 0
while running:
	for event in pg.event.get():
		if event.type == QUIT:
			running = False
		elif event.type == KEYDOWN:
			if event.key == K_w:
				if rot_type[-1] == 'l' or rot_type[-1] == 'r':
					rot_type = rot_type[-1] + 'u'
					rot_end = False
			elif event.key == K_s:
				if rot_type[-1] == 'l' or rot_type[-1] == 'r':
					rot_type = rot_type[-1] + 'd'
					rot_end = False
			elif event.key == K_a:
				if rot_type[-1] == 'u' or rot_type[-1] == 'd':
					rot_type = rot_type[-1] + 'l'
					rot_end = False	
			elif event.key == K_d:
				if rot_type[-1] == 'u' or rot_type[-1] == 'd':
					rot_type = rot_type[-1] + 'r'
					rot_end = False
	screen.fill(BLACK)

	# 먹이가 없다면 정해진 시간 후에 먹이를 놓는다
	if not something:
		print(something, pg.time.get_ticks(), start_t)
		if pg.time.get_ticks() - start_t > 3000:
			prey = Rect(randint(body_size *2 , w -body_size * 2), 
				randint(body_size *2, h - body_size*2), body_size, body_size)
			something = True

	# 먹이를 그린다
	pg.draw.rect(screen, YELLOW, prey, 0) 
	# 스네이크를 그린다
	for i in range(len(snake_body)):
		pg.draw.rect(screen, GREEN, snake_body[i], 0)
	
	pg.display.update() 
	# 스네이크를 정해진 방향대로 이동시킨다
	if rot_end == False:
		if rot_type == 'lu':
			for i in range(j+1):
				snake_body[i][1] -= body_size
			for i in range(j+1, len(snake_body)):
				snake_body[i][0] -= body_size
		elif rot_type == 'ru':
			for i in range(j+1):
				snake_body[i][1] -= body_size
			for i in range(j+1, len(snake_body)):
				snake_body[i][0] += body_size
		elif rot_type == 'ld':
			for i in range(j+1):
				snake_body[i][1] += body_size
			for i in range(j+1, len(snake_body)):
				snake_body[i][0] -= body_size
		elif rot_type == 'rd':
			for i in range(j+1):
				snake_body[i][1] += body_size
			for i in range(j+1, len(snake_body)):
				snake_body[i][0] += body_size
		elif rot_type == 'ul':
			for i in range(j+1):
				snake_body[i][0] -= body_size
			for i in range(j+1, len(snake_body)):
				snake_body[i][1] -= body_size
		elif rot_type == 'ur':
			for i in range(j+1):
				snake_body[i][0] += body_size
			for i in range(j+1, len(snake_body)):
				snake_body[i][1] -= body_size
		elif rot_type == 'dl':
			for i in range(j+1):
				snake_body[i][0] -= body_size
			for i in range(j+1, len(snake_body)):
				snake_body[i][1] += body_size
		elif rot_type == 'dr':
			for i in range(j+1):
				snake_body[i][0] += body_size
			for i in range(j+1, len(snake_body)):
				snake_body[i][1] += body_size
	
	else:
		if rot_type[-1] == 'u':
			for i in range(len(snake_body)):
				snake_body[i][1] -= body_size   
		elif rot_type[-1] == 'd':
			for i in range(len(snake_body)):
				snake_body[i][1] += body_size   		
		elif rot_type[-1] == 'l':
			for i in range(len(snake_body)):
				snake_body[i][0] -= body_size     
		elif rot_type[-1] == 'r':
			for i in range(len(snake_body)):
				snake_body[i][0] += body_size

	
	if something and collide(snake_body[0], prey):
		if rot_type[-1] == 'u':
			tail = Rect(snake_body[-1][0], snake_body[-1][1] + body_size, body_size, body_size)   
		elif rot_type[-1] == 'd':
			tail = Rect(snake_body[-1][0], snake_body[-1][1] - body_size, body_size, body_size)   		
		elif rot_type[-1] == 'l':
			tail = Rect(snake_body[-1][0] + body_size, snake_body[-1][1], body_size, body_size)     
		elif rot_type[-1] == 'r':
			tail = Rect(snake_body[-1][0] - body_size, snake_body[-1][1], body_size, body_size)
		snake_body.append(tail)
		prey[0] = -1000
		prey[1] = -1000
		something = False
		start_t = pg.time.get_ticks()
	
	if rot_end == False:
		j += 1
		if j == len(snake_body):
			j = 0
			rot_end = True 
	clock.tick(15)   