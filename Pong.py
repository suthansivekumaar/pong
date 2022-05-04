import pygame
import sys

pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
WIDTH = 700
HEIGHT = 700
radius = 20
player_1_x = 50
player_2_x = 600
player_1_y = 365
player_2_y = 365
score_1 = 0
score_2 = 0
ball_x = 340
ball_y = 340
ball_dx = 2
ball_dy = 2

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
	# ball moving
	ball_x += ball_dx	
	ball_y += ball_dy	

	# makes sure ball doesnt exit out of the frame
	# increments score if ball goes out of frame horizontally
	if ball_y <= 0:
		ball_dy *= -1

	if ball_y >= HEIGHT - 20:
		ball_dy *= -1

	if ball_x <= 0:
		score_2 += 1
		ball_x = 340
		ball_y = 340
		ball_dx *= -1
		ball_dy *= -1

	if ball_x >= HEIGHT - 20:
		score_1 += 1
		ball_x = 340
		ball_y = 340
		ball_dx *= -1
		ball_dy *= -1

	# makes sure player paddles doesn't move out of the frame
	if player_1_y <= 0:
		player_1_y = 0

	if player_1_y >= HEIGHT - 100:
		player_1_y = HEIGHT - 100

	if player_2_y <= 0:
		player_2_y = 0

	if player_2_y >= HEIGHT - 100:
		player_2_y = HEIGHT - 100

	# code for ball colliding with paddles
	if ((ball_x == (player_1_x + 20)) and ((ball_y >= player_1_y) and ((ball_y + 20) <= (player_1_y + 100))) and ball_y > 0 and ball_y < HEIGHT - 20):
		ball_dx *= -1
		ball_dy *= -1

	if (((ball_x + 20) == (player_2_x)) and ((ball_y >= player_2_y) and ((ball_y + 20) <= (player_2_y + 100)))):
		ball_dx *= -1
		ball_dy *= -1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			# move up player 1
			if event.key == pygame.K_w:
				player_1_y -= 80

			# move down player 1
			if event.key == pygame.K_s:
				player_1_y += 80

			# move up player 2
			if event.key == pygame.K_UP:
				player_2_y -= 80

			# move down player 2
			if event.key == pygame.K_DOWN:
				player_2_y += 80

	clock.tick(30)
	screen.fill(BLACK)
	# player 1 paddle
	pygame.draw.rect(screen, WHITE, (player_1_x,player_1_y,20,100))
	# player 2 paddle
	pygame.draw.rect(screen, WHITE, (player_2_x,player_2_y,20,100))
	# middle dashed line
	for x in range(-60, 700, 60):
		pygame.draw.rect(screen, WHITE, (340,x + 60,20,40))
	# ball
	pygame.draw.rect(screen, WHITE, (ball_x,ball_y,20,20))

	# score for player 1
	font = pygame.font.Font('freesansbold.ttf', 32)
	text = font.render(str(score_1), True, WHITE)

	textRect = text.get_rect()
	textRect.center = (250, 50)
	screen.blit(text, textRect)

	# score for player 2
	font2 = pygame.font.Font('freesansbold.ttf', 32)
	text2 = font.render(str(score_2), True, WHITE)

	textRect2 = text.get_rect()
	textRect2.center = (450, 50)
	screen.blit(text2, textRect2)

	pygame.display.update()