import pygame

WHITE = (255, 255, 255)
BLACK = (0 ,0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
CYAN = (255, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
pygame.init()
clock = pygame.time.Clock()
w, h = 800, 600

num_body = 3
body_size = 10
gap = 2
snake_body = []
for i in range(num_body):
    snake_rect = [w//2 + i *body_size + i*2, h//2, body_size, body_size]
    snake_body.append(snake_rect)
screen = pygame.display.set_mode((w,h))
running = True
rot_type = 'l'
rot_end = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_w:
                rot_type = 'u'
                rot_end = False
            elif event.key == pygame.K_s:
                rot_type = 'd'
            elif event.key == pygame.K_a:
                rot_type = 'l'
            elif event.key == pygame.K_d:
                rot_type = 'r'
    screen.fill(BLACK)
    # 스네이크를 그린다
    for i in range(num_body):
        pygame.draw.rect(screen, GREEN, snake_body[i], 0)
    
    pygame.display.update() 
    # 스네이크를 왼쪽으로 전진시킨다
    if rot_type == 'l':
        for i in range(num_body):
            snake_body[i][0] -= body_size
    elif rot_type == 'r':
        snake_body = snake_body[::-1]
        for i in range(num_body):
            snake_body[i][0] += body_size
    if rot_type == 'u':
        if rot_end == False:
            for j in range(num_body):    
                if j == 0:
                    for i in range(num_body):
                        if i == 0:
                            snake_body[i][0] -= body_size
                            snake_body[i][1] -= body_size
                        else:
                            snake_body[i][0] -= body_size
                elif j == 1:
                    for i in range(num_body):
                        if i == 0:
                            snake_body[i][1] -= body_size
                        elif i== 1:
                            snake_body[i][0] -= body_size
                            snake_body[i][1] -= body_size
                        else:
                            snake_body[i][0] -= body_size
                elif j == 1:
                    for i in range(num_body):
                        if i == 0:
                            snake_body[i][1] -= body_size
                        elif i== 1:
                            snake_body[i][1] -= body_size
                        else:
                            snake_body[i][0] -= body_size
                            snake_body[i][1] -= body_size
            rot_end = True
        else:
            for i in range(num_body):
                snake_body[i][1] -= body_size           
    clock.tick(12)   
